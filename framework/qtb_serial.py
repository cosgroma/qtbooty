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

  def __init__(self, *args):
    super(SerialWidget, self).__init__()
    self.ser = None
    # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
    # sizePolicy.setHorizontalStretch(1)
    # sizePolicy.setVerticalStretch(1)
    # self.setSizePolicy(sizePolicy)
    self.reader = CReader()
    self.writer = CWriter()

    # QMainWindow.__init__(*(self, ) + args)
    self.ui = Ui_MainWindow()
    self.setupUi()
    self.printInfo("Ready...")

  def setupUi(self):
    self.ui.setupUi(self)
    self.ui.baudRateComboBox.addItems(baudRates)
    self.refreshPorts()
    QObject.connect(self.ui.exitPushButton, SIGNAL("clicked()"), self, SLOT("close()"))
    QObject.connect(self.ui.refreshPortsPushButton, SIGNAL("clicked()"), self.refreshPorts)
    QObject.connect(self.ui.connectPushButton, SIGNAL("clicked()"), self.connect)
    QObject.connect(self.ui.disconnectPushButton, SIGNAL("clicked()"), self.disconnect)
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
    self.disconnect()
    try:
      self.printInfo("Connecting to %s with %s baud rate." %
                     (self.getSelectedPort(), self.getSelectedBaudRate()))
      self.ser = serial.Serial(str(self.getSelectedPort()),
                               int(self.getSelectedBaudRate()))
      self.startReader(self.ser)
      self.printInfo("Connected successfully.")
    except:
      self.ser = None
      self.printError("Failed to connect!")

  def disconnect(self):
    self.stopThreads()
    if self.ser is None:
      return
    try:
      if self.ser.isOpen:
        self.ser.close()
        self.printInfo("Disconnected successfully.")
    except:
      self.printError("Failed to disconnect!")
    self.ser = None

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
    self.ui.logPlainTextEdit.insertPlainText(text)
    self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

  def processCmd(self):
    cmd = self.ui.cmdLineEdit.text()
    self.printCmd(cmd)
    self.writer.start(self.ser, cmd)
    self.ui.cmdLineEdit.clear()

  def closeEvent(self, event):
    self.disconnect()


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
  mainWindow = SerialWidget()
  mainWindow.show()
  sys.exit(app.exec_())
