import sys
import serial
import glob
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QMainWindow, QTextCursor, QWidget
from PyQt4.QtCore import QObject, SIGNAL, SLOT, QThread
from mainWindow import Ui_MainWindow

baudRates = ['9600',
             '38400',
             '115200',
             '1200000', ]


class SerialWidget(QWidget):

  def __init__(self, port=None, baud=None, connect_on_start=False):
    super(SerialWidget, self).__init__()
    self.ser = None
    self.reader = CReader()
    self.writer = CWriter()
    self.ui = Ui_MainWindow()
    self.setupUi()
    self.connected = False

    if port is not None:
      curIndex = self.ui.portsComboBox.findText(port)
      if curIndex > -1:
        self.ui.portsComboBox.setCurrentIndex(curIndex)
        self.port = port
    if baud is not None and baud in baudRates:
      self.ui.baudRateComboBox.setCurrentIndex(self.ui.baudRateComboBox.findText(baud))
      self.baud = baud

    if connect_on_start and self.baud is not None and self.port is not None:
      self.connect()

  def setupUi(self):
    self.ui.setupUi(self)
    self.ui.baudRateComboBox.addItems(baudRates)
    self.refreshPorts()

    # QObject.connect(self.ui.exitPushButton, SIGNAL("clicked()"), self, SLOT("close()"))
    QObject.connect(self.ui.refreshPortsPushButton, SIGNAL("clicked()"), self.refreshPorts)
    QObject.connect(self.ui.connectPushButton, SIGNAL("clicked()"), self.connect)
    # QObject.connect(self.ui.disconnectPushButton, SIGNAL("clicked()"), self.disconnect)
    QObject.connect(self.ui.cmdLineEdit, SIGNAL("returnPressed()"), self.processCmd)

    QObject.connect(self.reader, SIGNAL("newData(QString)"), self.updateLog)
    QObject.connect(self.reader, SIGNAL("error(QString)"), self.printError)
    QObject.connect(self.writer, SIGNAL("error(QString)"), self.printError)

  def getUSBPorts(self):
    return glob.glob("/dev/ttyUSB*")

  def getSPPorts(self):
    return glob.glob("/dev/ttyS*")

  def getWinPorts(self):
    return ["COM1", "COM2", "COM3", "COM5"]

  def getSelectedPort(self):
    return self.ui.portsComboBox.currentText()

  def getSelectedBaudRate(self):
    return self.ui.baudRateComboBox.currentText()

  def refreshPorts(self):
    self.ui.portsComboBox.clear()
    self.ui.portsComboBox.addItems(sorted(self.getUSBPorts()))
    self.ui.portsComboBox.addItems(sorted(self.getSPPorts()))
    self.ui.portsComboBox.addItems(sorted(self.getWinPorts()))

  def connect(self):
    if self.connected:
      self.connected = False
      self.stopThreads()
      self.ui.connectPushButton.setText("connect")
      self.ui.connectPushButton.setDown(False)
      if self.ser.isOpen:
        self.ser.close()
        self.setWindowTitle("disconnected")
      self.ser = None
    else:
      self.ui.connectPushButton.setDown(True)
      self.ui.connectPushButton.setText("disconnect")
      self.setWindowTitle("%s:%s" % (self.getSelectedPort(), self.getSelectedBaudRate()))
      try:
        # self.ui.setWindowTitle("%s:%s" % (self.getSelectedPort(), self.getSelectedBaudRate()))
        self.ser = serial.Serial(str(self.getSelectedPort()), int(self.getSelectedBaudRate()))
        self.ser.write("\n")
        self.connected = True
        self.startReader(self.ser)
      except:
        self.ser = None
        self.connected = False
        self.printError("ERROR")

  def startReader(self, ser):
    self.reader.start(ser)

  def stopThreads(self):
    self.stopReader()
    self.stopWriter()

  def stopReader(self):
    if self.reader.isRunning():
      self.reader.terminate()

  def stopWriter(self):
    if self.writer.isRunning():
      self.writer.terminate()

  def printInfo(self, text):
    self.ui.logPlainTextEdit.appendPlainText(text)
    self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

  def printError(self, text):
    self.ui.logPlainTextEdit.appendPlainText(text)
    self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

  def printCmd(self, text):
    self.ui.logPlainTextEdit.appendPlainText("> " + text + "\n")
    self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

  def updateLog(self, text):
    self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)
    # print([text])
    ptext = str(text)
    if '\n' in ptext:
      ptext = '\n'.join(filter(None, ptext.splitlines()))
    if (len(ptext) < 4 and '->' in ptext) or "[vxWorks *]#" in ptext:
      ptext = '\n' + ptext + '\n'
    else:
      ptext += '\n'
    # if not '->' == ptext[0:1] and ptext[-1] is not '\n':
    #   ptext += '\n'
    # print([ptext])
    self.ui.logPlainTextEdit.insertPlainText(ptext)
    self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

  def processCmd(self):
    cmd = self.ui.cmdLineEdit.text()
    self.writer.start(self.ser, cmd)
    self.ui.cmdLineEdit.clear()

  def closeEvent(self, event):
    pass


class CReader(QThread):

  def start(self, ser, priority=QThread.InheritPriority):
    self.ser = ser
    QThread.start(self, priority)

  def run(self):
    while True:
      try:
        data = self.ser.read(1)
        n = self.ser.inWaiting()
        if n:
          data = data + self.ser.read(n)
        self.emit(SIGNAL("newData(QString)"), data)
      except:
        errMsg = "Reader thread is terminated unexpectedly."
        self.emit(SIGNAL("error(QString)"), errMsg)
        break


class CWriter(QThread):

  def start(self, ser, cmd="", priority=QThread.InheritPriority):
    self.ser = ser
    self.cmd = cmd
    QThread.start(self, priority)

  def run(self):
    try:
      self.ser.write(str(self.cmd) + "\n")
    except:
      errMsg = "Writer thread is terminated unexpectedly."
      self.emit(SIGNAL("error(QString)"), errMsg)

  def terminate(self):
    self.wait()
    QThread.terminate(self)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  mainWindow = SerialWidget(port="COM5", baud="115200", connect_on_start=True)
  mainWindow.show()
  sys.exit(app.exec_())
