
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import collections

from QtBooty import graphs
from QtBooty import App

from phasor.analysis import Spectrum

length = 5120
numpoints = 4096
maxlen = 200

dq = collections.deque(maxlen=maxlen)
imgdata = np.zeros((numpoints/2 + 1, maxlen))

ts = np.linspace(0, 120, length)
acc = lambda t: 10*np.sin(2*np.pi*2.0*t) + 5*np.sin(2*np.pi*(10.0)*t) + 5*np.sin(2*np.pi*(8.0+np.random.random())*t) + 10*np.random.random(len(t))
fs = ts[1]-ts[0]

spec = Spectrum(fs, length, numpoints)
f, p = spec.get_fft(acc(ts))

app = App()

gv = pg.GraphicsView()
l = QtGui.QGraphicsGridLayout()
l.setHorizontalSpacing(0)
l.setVerticalSpacing(-30)

vb = pg.ViewBox()
vb2 = pg.ViewBox()

p1 = pg.PlotDataItem(pen='r', fillLevel=0, brush=(0, 0, 255, 80), downsample=True)

img = pg.ImageItem(imgdata)
xScale = pg.AxisItem(orientation='bottom', linkView=vb)
yScale = pg.AxisItem(orientation='left', linkView=vb)
xScale.setScale((fs/2)/(numpoints/2 + 1))
w = pg.HistogramLUTItem()
w.setImageItem(img)

vb.addItem(p1)
vb2.addItem(img)
l.addItem(yScale, 0, 0)
l.addItem(vb, 0, 1)
l.addItem(xScale, 1, 1)
l.addItem(vb2, 2, 1)
l.addItem(w, 0, 2, 3, 1)
vb2.setXLink(vb)
gv.centralWidget.setLayout(l)

def update():
  global spec, acc, img, ts, fs, length
  f, p = spec.get_fft(acc(ts))
  ts += length/fs
  dq.append(p)
  imgdata[:, -len(dq):] = np.matrix(dq).transpose()
  img.setImage(imgdata, autoHistogramRange=False, autoRange=False, autoLevels=False)
  p1.setData(p)

app.add_widget(gv)
app.add_timer(100, update)
app.run()


# app.add_widget(w)
# yScale = pg.AxisItem(orientation='left', linkView=vb)
# l.addItem(yScale, 0, 0)
# xScale.setLabel(text="<span style='color: #ff0000; font-weight: bold'>X</span> <i>Axis</i>", units="s")
# yScale.setLabel('Y Axis', units='V')

