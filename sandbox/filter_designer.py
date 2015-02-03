
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import collections

from QtBooty import graphs
from QtBooty import App
from QtBooty import framework

from functools import partial

import scipy.signal as signal


class FilterDesigner(object):
  """docstring for FilterDesigner"""
  def __init__(self):
    super(FilterDesigner, self).__init__()
    self.setup_control()
    self.setup_plots()

    self.coeffs = []
    self.config = {
      "taps":    100,
      "cutoff":  [.5],
      "window":  "hanning"
    }

  def setup_control(self):
    self.iogrid = framework.IOGrid()
    self.params = self.iogrid.load_config_file('filter_designer_io.json')
    self.iogrid.connect_changed_callback(self.onChange)

  def get_io_widget(self):
    return self.iogrid

  def get_plot_widget(self):
    return self.tabs

  def setup_plots(self):

    self.tabs = framework.Tabs()

    self.pw1 = pg.PlotWidget()
    self.pw1.showGrid(x=True, y=True)

    self.pw2 = pg.PlotWidget()
    self.pw2.showGrid(x=True, y=True)

    self.pw3 = pg.PlotWidget()
    self.pw3.showGrid(x=True, y=True)

    self.tabs.add_tab(self.pw1, 'Magnitude Response')
    self.tabs.add_tab(self.pw2, 'Phase Response')
    self.tabs.add_tab(self.pw3, 'Impulse Response')

  def onChange(self, param, changes):

    for param, change, data in changes:
      childName = param.name()
      print('  parameter: %s' % childName)
      print('  change:    %s' % change)
      print('  data:      %s' % str(data))
      print('  ----------')

      if param.name() == "setadd":
        fset = [
          self.params["fstart"],
          self.params["fstop"],
          self.params["atten"],
          "delete"
        ]
        self.iogrid.update_widget("ftable", fset)
      # if param.name() == "visual":
      #   region1 = pg.LinearRegionItem(brush=(254, 10, 100, 50))
      #   region1.sigRegionChanged.connect(partial(region_update, region))
      #   minX, maxX = region.getRegion()

  def create_filter(self, **kwargs):
    self.config.update(kwargs)
    self.coeffs = signal.firwin(**self.config)

  def compute_freq_response(self):
    self.freq, self.mag = signal.freqz(self.coeffs)
    self.angles = np.unwrap(np.angle(self.mag))

  def impulse_response(self):
    l = len(self.coeffs)
    impulse = np.zeros(l)
    impulse[0] = 1.
    self.t = np.linspace(0, l, l)
    self.response = signal.lfilter(self.coeffs, 1, impulse)

  def update(self):
    pass

  def update_plot(self):
    self.pw1.plot(self.freq, 20*np.log10(np.abs(self.mag)), pen='r')
    self.pw2.plot(self.freq, self.angles, pen='g')
    self.pw3.plot(self.t, self.impluse, pen=(200, 200, 200), symbolBrush=(255, 0, 0), symbolPen='w')



app = App()

fdesign = FilterDesigner()

tabs = fdesign.get_plot_widget()
iogrid = fdesign.get_io_widget()

app.add_widget(tabs)
app.add_widget(iogrid)
app.run()
