
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import collections

from QtBooty import graphs
from QtBooty import App
from QtBooty import framework

import scipy.signal as signal

configdict = {
  "layout": ["h", "na"],
  "groups": [
    {
      "box_enabled": True,
      "box_name": "Filter Designer",
      "layout": [
        "v",
        "na"
      ],
      "items": [
        {
          "class": "button",
          "name": "custom region",
          "label": "Custom Region"
        }
      ]
    }
  ]
}

def compute_freq_response(b):
  w, h = signal.freqz(b)
  a = np.unwrap(np.angle(h))
  return w, h, a

def create_plot(gv, title="", xlabel="", xunits="", ylabel="", yunits="", grid=True, loc=(0,0)):
  p = gv.addPlot(*loc, title=title)
  if grid: p.showGrid(x=True, y=True)
  p.setLabel('left', ylabel, units=yunits)
  p.setLabel('bottom', xlabel, units=xunits)
  return p

b = signal.firwin(40, 0.5)

w, h, a = compute_freq_response(b)

class FilterDesigner(object):
  """docstring for FilterDesigner"""
  def __init__(self, arg):
    super(FilterDesigner, self).__init__()
    self.arg = arg
    self.iogrid = framework.IOGrid()
    self.params = self.iogrid.load_config(configdict)
  def update(self):
    pass




app = App()
gv1 = pg.GraphicsLayoutWidget()
p1 = create_plot(gv1, "Frequency Response", "Freqeuncy", "MHz", "Magnitude", "dB")
p1.plot(w, 20*np.log10(np.abs(h)), pen='r')

gv2 = pg.GraphicsLayoutWidget()
p2 = create_plot(gv, "Phase Response", "Freqeuncy", "MHz", "Phase", "Radians")
p2.plot(w, a, pen='g')


# region1 = pg.LinearRegionItem(brush=(254, 10, 100, 50))
# region2 = pg.LinearRegionItem()

# # region1.sigRegionChanged.connect(update)
# # minX, maxX = region.getRegion()

# p1.addItem(region1, ignoreBounds=True)
# p1.addItem(region2, ignoreBounds=True)

tabs = framework.Tabs()
tabs.add_tab(gv1)
tabs.add_tab(gv2)
app.add_widget(gv)
app.add_widget(iogrid)
app.run()


# """
# Demonstrates some customized mouse interaction by drawing a crosshair that follows
# the mouse.


# """

# import initExample ## Add path to library (just for examples; you do not need this)
# import numpy as np
# import pyqtgraph as pg
# from pyqtgraph.Qt import QtGui, QtCore
# from pyqtgraph.Point import Point

# #generate layout
# app = QtGui.QApplication([])
# win = pg.GraphicsWindow()
# win.setWindowTitle('pyqtgraph example: crosshair')
# label = pg.LabelItem(justify='right')
# win.addItem(label)
# p1 = win.addPlot(row=1, col=0)
# p2 = win.addPlot(row=2, col=0)

# region = pg.LinearRegionItem()
# region.setZValue(10)
# # Add the LinearRegionItem to the ViewBox, but tell the ViewBox to exclude this
# # item when doing auto-range calculations.
# p2.addItem(region, ignoreBounds=True)

# #pg.dbg()
# p1.setAutoVisible(y=True)


# #create numpy arrays
# #make the numbers large to show that the xrange shows data from 10000 to all the way 0
# data1 = 10000 + 15000 * pg.gaussianFilter(np.random.random(size=10000), 10) + 3000 * np.random.random(size=10000)
# data2 = 15000 + 15000 * pg.gaussianFilter(np.random.random(size=10000), 10) + 3000 * np.random.random(size=10000)

# p1.plot(data1, pen="r")
# p1.plot(data2, pen="g")

# p2.plot(data1, pen="w")

# def update():
#     region.setZValue(10)
#     minX, maxX = region.getRegion()
#     p1.setXRange(minX, maxX, padding=0)

# region.sigRegionChanged.connect(update)

# def updateRegion(window, viewRange):
#     rgn = viewRange[0]
#     region.setRegion(rgn)

# p1.sigRangeChanged.connect(updateRegion)

# region.setRegion([1000, 2000])

# #cross hair
# vLine = pg.InfiniteLine(angle=90, movable=False)
# hLine = pg.InfiniteLine(angle=0, movable=False)
# p1.addItem(vLine, ignoreBounds=True)
# p1.addItem(hLine, ignoreBounds=True)


# vb = p1.vb

# def mouseMoved(evt):
#     pos = evt[0]  ## using signal proxy turns original arguments into a tuple
#     if p1.sceneBoundingRect().contains(pos):
#         mousePoint = vb.mapSceneToView(pos)
#         index = int(mousePoint.x())
#         if index > 0 and index < len(data1):
#             label.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>" % (mousePoint.x(), data1[index], data2[index]))
#         vLine.setPos(mousePoint.x())
#         hLine.setPos(mousePoint.y())



# proxy = pg.SignalProxy(p1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
# #p1.scene().sigMouseMoved.connect(mouseMoved)


# ## Start Qt event loop unless running in interactive mode or using pyside.
# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtGui.QApplication.instance().exec_()
