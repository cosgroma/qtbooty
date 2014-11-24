#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-26 08:54:11
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2014-11-26 11:03:10


from PyQt4 import QtCore, QtGui, QtDeclarative

class DialControl(QtCore.QObject):

  updated = QtCore.pyqtSignal()

  def __init__(self):
    super(DialControl, self).__init__()
    self.timer = QtCore.QTimer()
    self.timer.setInterval(1000)
    self.timer.timeout.connect(self.sliderUpdate)
    self._sliderValue = 0


  def sliderUpdate(self):
    self._sliderValue += 1
    print "EMIT:", self._sliderValue
    self.updated.emit()

  @QtCore.pyqtSlot(int)
  def sliderPrint(self, value):
      print "slider value"
      print "Timer Started"
      self.timer.start()
      return True

  @QtCore.pyqtProperty(int, notify=updated)
  def sliderValue(self):
    return self._sliderValue


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    canvas = QtDeclarative.QDeclarativeView()
    engine = canvas.engine()

    control = DialControl()
    engine.rootContext().setContextObject(control)
    canvas.setSource(QtCore.QUrl.fromLocalFile('dialcontrol.qml'))
    # engine.quit.connect(app.quit)

    canvas.setGeometry(QtCore.QRect(100, 100, 450, 450))
    canvas.show()

    sys.exit(app.exec_())
