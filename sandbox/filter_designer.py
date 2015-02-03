
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import collections

from QtBooty import graphs
from QtBooty import App
from QtBooty import framework

import scipy.signal as signal

configdict = {
  "layout": ["v", "na"],
  "groups": [
    {
      "box_enabled": True,
      "box_name": "Filter Parameters",
      "layout": [
        "h",
        "na"
      ],
      "items": [
        {
          "class": "edit",
          "name": "fs",
          "label": "Sample Frequency (MHz)",
          "tool-tip": "Source Sample Frequency",
          "dtype": "float"
        },
        {
          "class": "edit",
          "name": "nfreqs",
          "label": "N-Freqs",
          "tool-tip": "The size of the interpolation mesh used to construct the filter",
          "dtype": "int"
        },
        {
          "class": "combo",
          "name": "window",
          "items": ["hamming", "boxcar", "triang", "blackman", "hamming", "hann", "bartlett", "flattop", "parzen", "bohman", "blackmanharris", "nuttall", "barthann"],
          "label": "Window Function",
          "tool-tip": "Window function to use. Default is hamming",
          "dtype": "int",
          "maxVisible": 4
        },
        {
          "class": "button",
          "qtype": "check",
          "label": "Asymetric",
          "name": "asym"
        }
      ]
    },
    {
      "box_enabled": True,
      "box_name": "Filter Response Configuration",
      "layout": [
        "h",
        "na"
      ],
      "items": [
        {
          "class": "button",
          "name": "manual",
          "label": "",
          "tool-tip": "Manually Configure Filter Bands",
          "dtype": "float"
        }
      ]
    }
  ]
}



def compute_freq_response(b):
  w, h = signal.freqz(b)
  a = np.unwrap(np.angle(h))
  return w, h, a

def impulse_response(b, a=1):
  l = len(b)
  impulse = np.zeros(l)
  impulse[0] = 1.
  x = np.linspace(0, l, l)
  response = signal.lfilter(b, a, impulse)
  return x, response

def create_gv_plot(gv, title="", xlabel="", xunits="", ylabel="", yunits="", grid=True, loc=(0,0)):
  p = gv.addPlot(*loc, title=title)
  if grid: p.showGrid(x=True, y=True)
  p.setLabel('left', ylabel, units=yunits)
  p.setLabel('bottom', xlabel, units=xunits)
  return p

def create_plot(pw, title="", xlabel="", xunits="", ylabel="", yunits="", grid=True):
  if grid: p.showGrid(x=True, y=True)
  p.setLabel('left', ylabel, units=yunits)
  p.setLabel('bottom', xlabel, units=xunits)
  return p

# def create_fir(taps=400, object):


taps = 100
# Low Pass
b = signal.firwin(taps, 0.5)
# High Pass
b = signal.firwin(taps, cutoff = 0.3, window = "hanning")
w, h, a = compute_freq_response(b)

x, impluse = impulse_response(b)
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

pw1 = pg.PlotWidget()
pw1.showGrid(x=True, y=True)
pw1.plot(w, 20*np.log10(np.abs(h)), pen='r')

pw2 = pg.PlotWidget()
pw2.showGrid(x=True, y=True)
pw2.plot(w, a, pen='g')

pw3 = pg.PlotWidget()
pw3.plot(x, impluse, pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')


# region1 = pg.LinearRegionItem(brush=(254, 10, 100, 50))
# region2 = pg.LinearRegionItem()

# # region1.sigRegionChanged.connect(update)
# # minX, maxX = region.getRegion()

# p1.addItem(region1, ignoreBounds=True)
# p1.addItem(region2, ignoreBounds=True)widget

def changed(change):
  print "yo"

tabs = framework.Tabs()
tabs.add_tab(pw1, 'Magnitude Response')
tabs.add_tab(pw2, 'Phase Response')
tabs.add_tab(pw3, 'Impulse Response')

app.add_widget(tabs)

iogrid = framework.IOGrid()
params = iogrid.load_config(configdict)
iogrid.connect_changed_callback(changed)
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
