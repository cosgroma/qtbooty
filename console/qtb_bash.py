import sys
import glob
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QMainWindow, QTextCursor, QWidget
from PyQt4.QtCore import QObject, SIGNAL, SLOT, QThread
from mainWindowBash import Ui_MainWindow
import subprocess
import time

import os


class BashWidget(QWidget):

  def __init__(self, cwd="c:/cygwin64/home/cosgrma"):
    super(BashWidget, self).__init__()
    self.ui = Ui_MainWindow()
    self.setupUi()
    self.bash = None
    self.cwd = cwd

  def setupUi(self):
    self.ui.setupUi(self)
    QObject.connect(self.ui.cmdLineEdit, SIGNAL("returnPressed()"), self.processCmd)

  def printInfo(self, text):
    self.ui.logPlainTextEdit.appendPlainText(text)
    self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

  def printError(self, text):
    self.ui.logPlainTextEdit.appendPlainText(text)
    self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

  def printCmd(self, text):
    self.ui.logPlainTextEdit.appendPlainText(text)
    self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

  def updateLog(self, text):
    self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)
    self.ui.logPlainTextEdit.insertPlainText(text)
    self.ui.logPlainTextEdit.moveCursor(QTextCursor.End)

  def processCmd(self):
    self.bash = subprocess.Popen(['bash'], cwd=self.cwd, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmd = self.ui.cmdLineEdit.text()
    data = self.bash.communicate("%s" % (cmd,))

    print self.cwd
    if len(data[0]) > 0:
      self.printCmd("$ %s\n" % (cmd,))
      self.updateLog("%s\n" % (data[0],))
    else:
      self.printCmd("$ %s" % (cmd,))

    self.ui.cmdLineEdit.clear()
    if cmd[0:2] == "cd" and len(data[1]) == 0:
      path = str(cmd.split(' ')[1])
      if path == "~":
        path = "c:/cygwin64/home/cosgrma"

      if path[0:4] == "c:/":
        self.cwd = path
      else:
        self.cwd += '/' + path

  def closeEvent(self, event):
    pass


if __name__ == "__main__":
  app = QApplication(sys.argv)
  mainWindow = BashWidget()
  mainWindow.show()
  sys.exit(app.exec_())
