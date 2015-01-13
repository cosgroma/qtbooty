#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-26 08:54:11
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2014-11-26 10:52:59


from PyQt4 import QtCore, QtGui, QtDeclarative

class DialBinding(QtCore.QObject):
  def __init__(self):
    super(DialBinding, self).__init__()
    self.timer = QtCore.QTimer()
    timer.setInterval(1000)
    timer.timeout.connect(self.sliderUpdate)
    self._sliderValue = 0

  def sliderUpdate(self):
    self._sliderValue += 1

  @QtCore.pyqtSlot(int)
  def sliderPrint(self, value):
      print value
      return True

  @QtCore.pyqtProperty(int)
  def sliderValue(self):
    return self._sliderValue


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    canvas = QtDeclarative.QDeclarativeView()
    engine = canvas.engine()

    bind = DialBinding()
    engine.rootContext().setContextObject(bind)
    canvas.setSource(QtCore.QUrl.fromLocalFile('dialcontrol.qml'))
    # engine.quit.connect(app.quit)

    canvas.setGeometry(QtCore.QRect(100, 100, 450, 450))
    canvas.show()

    sys.exit(app.exec_())
