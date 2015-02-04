
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
      "window":  "hamming"
    }

  def setup_control(self):

    self.iogrid = framework.IOGrid()
    self.params = self.iogrid.load_config_file('filter_designer_io.json')

    if self.params["window_function"] is None:
      self.params["window_function"] = "hamming"

    self.iogrid.set_groups_enabled([
      "Manual Filter Configuration",
      "Filter Description Table",
      "Visual Filter Configuration",
      "Filter Coefficent Generation"
    ], False)

    self.iogrid.connect_changed_callback(self.onParamChange)

  def get_io_widget(self):
    return self.iogrid

  def get_plot_widget(self):

    box = QtGui.QGroupBox()
    self.tabs.setSizePolicy(
      QtGui.QSizePolicy(
        QtGui.QSizePolicy.Preferred,
        QtGui.QSizePolicy.Preferred
      )
    )

    bl = QtGui.QGridLayout()
    bl.addWidget(self.tabs)
    box.setLayout(bl)
    return box

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


  def onParamChange(self, param, changes):

    if not hasattr(changes, '__getitem__'): return

    for param, change, data in changes:

      childName = param.name()
      print('  parameter: %s' % childName)
      print('  change:    %s' % change)
      print('  data:      %s' % str(data))
      print('  ----------')

      # Filter Definition
      if param.name() in ["taps", "fs"]:
        # Process Filter Defintion
        if self.params["taps"] not in [None, ""] and self.params["fs"] not in [None, ""]:

          self.iogrid.set_groups_enabled([
            "Manual Filter Configuration",
            "Filter Description Table",
            "Visual Filter Configuration"
          ], True)

          print "updates for the fir fitler"
          print "taps =", self.params["taps"]
          print "fs =", self.params["fs"]
          print "window_function =", self.params["window_function"]

        elif self.params["taps"] in [None, ""] or self.params["fs"] in [None, ""]:

          self.iogrid.set_groups_enabled([
            "Manual Filter Configuration",
            "Filter Description Table",
            "Visual Filter Configuration",
            "Filter Coefficent Generation"
          ], False)

      elif param.name() == "setadd":

        fset = [
          self.params["fstart"],
          self.params["fstop"],
          self.params["atten"]
        ]

        region = pg.LinearRegionItem()

        region.setZValue(10)

        region.setRegion([self.params["fstart"], self.params["fstop"]])
        self.pw1.addItem(region)

        self.iogrid.update_widget("ftable", fset, change)
        self.params["fstart"] = self.params["fstop"] = self.params["atten"] = ""


        p2.addItem(region, ignoreBounds=True)

      elif param.name() == "params":

        pass

      else:

        # region1 = pg.LinearRegionItem(brush=(254, 10, 100, 50))
        # region1.sigRegionParamChanged.connect(partial(region_update, region))object
        # minX, maxX = region.getRegion()
        print "runnint update widget"
        self.iogrid.update_widget(param.name(), data, change)


app = App()

fdesign = FilterDesigner()

tabs = fdesign.get_plot_widget()
iogrid = fdesign.get_io_widget()

app.add_widget(tabs)
app.add_widget(iogrid)

app.run()
