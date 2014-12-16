#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-26 08:54:11
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2014-11-26 21:51:33

import sys
sys.path.append('/Users/cosgroma/workspace/sergeant/guis')

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

import numpy as np
import pyqtgraph as pg

from QtBooty import App
from QtBooty import graphs
from QtBooty import framework

class Graph(QDeclarativeItem):
  def __init__(self):
    super(Graph, self).__init__()
    self.setFlag(QGraphicsItem.ItemHasNoContents, False)

    self.time_series = graphs.TimeSeries(interval=50, maxlen=100)
    self.time_series.run_test( interval=50, dynamic=True, freqs=[.1, .2, .3])
    mProxy = QGraphicsProxyWidget(self)
    mProxy.setWidget(self.time_series)
    self.time_series.show()

# class SdrController(QObject):

#   updated = pyqtSignal()

#   def __init__(self):
#     super(SdrController, self).__init__()

#     self.timer = QTimer()
#     self.timer.setInterval(1000)
#     self.timer.timeout.connect(self.sliderUpdate)
#     # self._sliderValue = 0



#   def sliderUpdate(self):
#     self._sliderValue += 1
#     print "EMIT:", self._sliderValue
#     self.updated.emit()

#   @pyqtSlot(int)
#   def sliderPrint(self, value):
#       print "slider value"
#       print "Timer Started"
#       self.timer.start()
#       return True

#   @pyqtProperty(int, notify=updated)
#   def sliderValue(self):
#     return self._sliderValue

#         #----------- self.setFlag(QGraphicsItem.ItemHasNoContents, False )





if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    qmlRegisterType(Graph, 'myPyQtGraph', 1, 0, 'PyQtGraph')

    canvas = QDeclarativeView()
    canvas.setSource(QUrl.fromLocalFile('sdrcontrol.qml'))

    canvas.setResizeMode(QDeclarativeView.SizeRootObjectToView)

    engine = canvas.engine()
    # control = SdrController()
    # engine.rootContext().setContextObject(control)
    # engine.quit.connect(app.quit)

    canvas.setGeometry(QRect(10, 10, 1191, 670))

    # rootObject = canvas.rootObject()
    # canvas.connect(canvas.engine() , SIGNAL('quit()') ,app.instance( ) , SLOT('quit()') )

    canvas.show()

    sys.exit(app.exec_())
