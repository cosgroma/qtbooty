

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

view = pg.GraphicsView()
l = pg.GraphicsLayout(border=(100,100,100))
p1 = l.addPlot()
p1.getAxis('bottom').setScale((fs/2)/(numpoints/2 + 1))
p1a = p1.plot(np.arange(0, numpoints/2 + 1), p)
l.nextRow()
p2 = l.addPlot()
img = pg.ImageItem(imgdata)
p2.addItem(img)
p2.getAxis('bottom').setScale((fs/2)/(numpoints/2 + 1))
p2.setXLink(p1)
p2.hideAxis('left')
view.setCentralItem(l)
view.resize(800,600)

def update():
  global spec, acc, img, ts, fs, length
  f, p = spec.get_fft(acc(ts))
  ts += length/fs
  dq.append(p)
  imgdata[: ,-len(dq):] = np.matrix(dq).transpose()
  img.setImage(imgdata, autoHistogramRange=False, autoRange=False, autoLevels=False)
  # npm = np.matrix([
  #   f,
  #   p
  # ])
  # fs_updater.add_data(npm, update.config)
  p1a.setData(p)


app.add_widget(view)
app.add_timer(30, update)
w = pg.HistogramLUTWidget()
w.setImageItem(img)
app.add_widget(w)
app.run()

# ## Title at top
# text = """
# This example demonstrates the use of GraphicsLayout to arrange items in a grid.<br>
# The items added to the layout must be subclasses of QGraphicsWidget (this includes <br>
# PlotItem, ViewBox, LabelItem, and GrphicsLayout itself).
# """
# l.addLabel(text, col=1, colspan=4)
# l.nextRow()

# ## Put vertical label on left side
# l.addLabel('Long Vertical Label', angle=-90, rowspan=3)

# ## Add 3 plots into the first row (automatic position)
# p1 = l.addPlot(title="Plot 1")
# p2 = l.addPlot(title="Plot 2")
# vb = l.addViewBox(lockAspect=True)
# img = pg.ImageItem(np.random.normal(size=(100,100)))
# vb.addItem(img)
# vb.autoRange()


# ## Add a sub-layout into the second row (automatic position)
# ## The added item should avoid the first column, which is already filled
# l.nextRow()
# l2 = l.addLayout(colspan=3, border=(50,0,0))
# l2.setContentsMargins(10, 10, 10, 10)
# l2.addLabel("Sub-layout: this layout demonstrates the use of shared axes and axis labels", colspan=3)
# l2.nextRow()
# l2.addLabel('Vertical Axis Label', angle=-90, rowspan=2)
# p21 = l2.addPlot()
# p22 = l2.addPlot()
# l2.nextRow()
# p23 = l2.addPlot()
# p24 = l2.addPlot()
# l2.nextRow()
# l2.addLabel("HorizontalAxisLabel", col=1, colspan=2)

# ## hide axes on some plots
# p21.hideAxis('bottom')
# p22.hideAxis('bottom')
# p22.hideAxis('left')
# p24.hideAxis('left')
# p21.hideButtons()
# p22.hideButtons()
# p23.hideButtons()
# p24.hideButtons()


# ## Add 2 more plots into the third row (manual position)
# p4 = l.addPlot(row=3, col=1)
# p5 = l.addPlot(row=3, col=2, colspan=2)

# ## show some content in the plots
# p1.plot([1,3,2,4,3,5])
# p2.plot([1,3,2,4,3,5])
# p4.plot([1,3,2,4,3,5])
# p5.plot([1,3,2,4,3,5])



# ## Start Qt event loop unless running in interactive mode.
# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtGui.QApplication.instance().exec_()
