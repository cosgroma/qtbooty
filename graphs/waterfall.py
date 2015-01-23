
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
jetcm = jet(256)

# import visvis as vv
# app = vv.use('pyqt4')

length = 5120
numpoints = 8192
maxlen = 1000

app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="Basic plotting examples")

# win.resize(numpoints/2 + 1, 300)
win.setWindowTitle('pyqtgraph example: Plotting')
# plt1 = win.addPlot()
# plt2 = win.addPlot()

dq = collections.deque(maxlen=maxlen)
imgdata = np.zeros((numpoints/2 + 1, maxlen))

ts = np.linspace(0, 120, length)
acc = lambda t: 10*np.sin(2*np.pi*2.0*t) + 5*np.sin(2*np.pi*8.0*t) + 10*np.random.random(len(t))
fs = ts[1]-ts[0]

spec = Spectrum(fs, length, numpoints)
f, p = spec.get_fft(acc(ts))

pmin = np.min(p)
pmax = np.max(p)
pmean = np.mean(p)
pstd = np.std(p)

z = np.linspace(-3.5, 3.5, 16, endpoint=True)
intervals = pmean + z*(pstd)
pbs = np.array([0.0] + [norm.cdf(intr, loc=pmean, scale=pstd) for intr in intervals])
lencm = len(jetcm)
pbsd = np.diff(pbs)
stepsize = np.mean(np.diff(intervals))
proportions = np.round(pbsd*lencm)
lendiff = sum(proportions) - lencm

for i in reversed(range(len(proportions))):
  if proportions[i] is not 0:
    if proportions[i] >= lendiff:
      proportions[i] -= lendiff
      lendiff = 0
      break
    else:
      lendiff -= proportions[i]
      proportions[i] = 0

steps = []
[steps.extend(np.linspace(intr, intr + stepsize, propor)) for intr, propor in zip(intervals, proportions)]


y, x = np.histogram(p, bins=np.linspace(pmin, pmax, 100))

print pmin
print pmax
# curve = pg.PlotCurveItem(x, y, stepMode=True, fillLevel=0, brush=(0, 0, 255, 80))
# plt1.addItem(curve)

# ## Now draw all points as a nicely-spaced scatter plot
# y = pg.pseudoScatter(p, spacing=2.0)
# #plt2.plot(p, stop, y, pen=None, symbol='o', symbolSize=5)
# plt2.plot(p, y, pen=None, symbol='o', symbolSize=5, symbolPen=(255,255,255,200), symbolBrush=(0,0,255,150))
  # p = np.sqrt(p*p)
  # p = p/np.max(p)value, ...


# a = vv.subplot(1,1,1)
# a.axis.visible = 0
# vv.axis("tight", axes=a)

# Enable antialiasing for prettier plots
# pg.setConfigOptions(antialias=True)

img = pg.ImageItem()
view = win.addViewBox()

# steps = np.linspace(-100, 90, len(jetcm))

clrmp = pg.ColorMap(steps, np.array([pg.colorTuple(pg.mkColor(hexcolor)) for hexcolor in jetcm]))
lut = clrmp.getLookupTable(-40, 90, 1024)
img.setLookupTable(lut)

dq = collections.deque(maxlen=maxlen)
imgdata = np.zeros( (numpoints/2 + 1, maxlen) )



view.addItem(img)


def update():
  global spec, acc, img, ts, fs, length
  f, p = spec.get_fft(acc(ts))
  ts += length/fs
  dq.append(p)
  imgdata[: , -len(dq): ] = np.matrix(dq).transpose()
  img.setImage(imgdata)

  # vv.imshow(imgdata, clim=(np.min(imgdata), np.max(imgdata)), cm=vv.CM_JET, axes=a)


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)

# vv.colorbar()
# app.Run()

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
  import sys
  if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
      QtGui.QApplication.instance().exec_()


# img = pg.ImageItem()
# view = win.addViewBox()

# steps = np.linspace(0.0, 1.0, len(jetcm))
# clrmp = pg.ColorMap(steps, np.array([pg.colorTuple(pg.mkColor(hexcolor)) for hexcolor in jetcm]))
# lut = clrmp.getLookupTable(0, 1.0, 1000)
# img.setLookupTable(lut)

# dq = collections.deque(maxlen=1000)
# imgdata = np.zeros( (numpoints/2 + 1, 300) )

# view.addItem(img)
# # Enable antialiasing for prettier plots
# pg.setConfigOptions(antialias=True)

# t = scipy.linspace(0,120,4000)
# acc = lambda t: 10*scipy.sin(2*pi*2.0*t) + 5*scipy.sin(2*pi*8.0*t) + 2*scipy.random.random(len(t))
# fs = t[1]-t[0]

# def update():
#   signal = acc(t)
#   f, p = np_psd(signal, fs)
#   p = np.sqrt(p*p)
#   p = p/np.max(p)
#   global dq, img
#   dq.append(p)
#   imgdata[: , -len(dq): ] = np.matrix(dq).transpose()
#   img.setImage(imgdata)



# # import initExample ## Add path to library (just for examples; you do not need this)
# import numpy as np
# import struct
# import scipy
# import scipy.fftpack
# import time
# from scipy import pi

# import collections

# from pyqtgraph.Qt import QtGui, QtCore
# import numpy as np
# import pyqtgraph as pg

# from QtBooty.utils import jet

# jetcm = jet(16)

# def np_psd(signal, fs):
#   p = 20*np.log10(np.abs(np.fft.rfft(signal, 4096)))
#   f = np.linspace(0, fs/2, len(p))
#   return (f, p)

# app = QtGui.QApplication([])

# win = pg.GraphicsWindow(title="Basic plotting examples")
# win.resize(2049, 300)
# win.setWindowTitle('pyqtgraph example: Plotting')

# img = pg.ImageItem()
# view = win.addViewBox()

# # STEPS = np.array([0, 0.4, 0.8, 0.9, 1.0])

# steps = np.linspace(0.0, 1.0, len(jetcm))
# clrmp = pg.ColorMap(steps, np.array([pg.colorTuple(pg.mkColor(hexcolor)) for hexcolor in jetcm]))
# lut = clrmp.getLookupTable(0, 1.0, 1000)
# img.setLookupTable(lut)

# dq = collections.deque(maxlen=300)
# imgdata = np.zeros( (2049, 300) )

# view.addItem(img)
# # Enable antialiasing for prettier plots
# pg.setConfigOptions(antialias=True)

# t = scipy.linspace(0,120,4000)
# acc = lambda t: 10*scipy.sin(2*pi*2.0*t) + 5*scipy.sin(2*pi*8.0*t) + 2*scipy.random.random(len(t))
# fs = t[1]-t[0]

# def update():
#   signal = acc(t)
#   f, p = np_psd(signal, fs)
#   p = np.sqrt(p*p)
#   p = p/np.max(p)
#   global dq, img
#   dq.append(p)
#   imgdata[: , -len(dq): ] = np.matrix(dq).transpose()
#   img.setImage(imgdata)

# timer = QtCore.QTimer()
# timer.timeout.connect(update)
# timer.start(25)

# ## Start Qt event loop unless running in interactive mode or using pyside.
# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtGui.QApplication.instance().exec_()
