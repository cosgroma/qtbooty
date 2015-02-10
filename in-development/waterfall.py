
import numpy as np
import struct
import time
import collections

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from scipy.stats import norm
from phasor.analysis import Spectrum
from QtBooty.utils import jet, cool
from QtBooty import graph

from QtBooty import App

jetcm = jet(256)

length = 5120
numpoints = 4096
maxlen = 200

app = App('../config/app_config.json')

freq_series = graph.Line(legend=False, controller=False)

gscheduler = graph.GraphScheduler()
fs_updater = gscheduler.add_graph(freq_series, maxlen=1, interval=100)

gv = pg.GraphicsView()
gw = pg.GraphicsLayoutWidget()

gw_view = gw.addViewBox()
img = pg.ImageView()
view = img.getView()
view.invertY(False)
view.setLimits(xMin=0, yMin=0, yMax=maxlen)
imgv = img.getImageItem()
gw_view.addItem(imgv)
hist = img.getHistogramWidget()
# img.getRoiPlot().hide()

dq = collections.deque(maxlen=maxlen)
imgdata = np.zeros((numpoints/2 + 1, maxlen))

ts = np.linspace(0, 120, length)
acc = lambda t: 10*np.sin(2*np.pi*2.0*t) + 5*np.sin(2*np.pi*(8.0+np.random.random())*t) + 10*np.random.random(len(t))
fs = ts[1]-ts[0]

spec = Spectrum(fs, length, numpoints)

dq = collections.deque(maxlen=maxlen)
imgdata = np.zeros( (numpoints/2 + 1, maxlen) )

def update():
  global spec, acc, img, ts, fs, length
  f, p = spec.get_fft(acc(ts))
  ts += length/fs
  dq.append(p)
  imgdata[: ,-len(dq):] = np.matrix(dq).transpose()
  imgv.setImage(imgdata, autoHistogramRange=False, autoRange=False, autoLevels=False)
  npm = np.matrix([
    f,
    p
  ])
  fs_updater.add_data(npm, update.config)

update.config = {
  "plots":[{
    "name": "fft",
    "plot kwargs": {
      "pen": 'r',
      "downsample": None,
      "fillLevel": 0,
      "brush": (0, 0, 255, 80)
    }
  }]
}
# app.add_widget(img)
# app.add_widget(view)

app.add_widget(freq_series)
app.add_widget(gw)
app.add_widget(hist)
app.add_timer(30, update)
# gscheduler.start()
gscheduler.start()
app.run()
