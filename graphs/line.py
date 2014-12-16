#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 22:27:47
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2014-12-05 22:25:07

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
# from PyQt4 import QtCore, QtGui, Qt
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
from collections import deque
import numpy as np

class TimeSeries(QtGui.QWidget):
  def __init__(self, name=None, controller=False, interval=1000, maxlen=1000,  ylim=[-1 , 1]):
    super(TimeSeries, self).__init__()
    self.maxlen=maxlen
    self.interval = interval
    self.ylim = ylim

    self.layout = QtGui.QHBoxLayout()
    self.graph = LineGraph(name=name, maxlen=maxlen)

    self.graph.set_ylim(self.ylim)

    self.layout.addWidget(self.graph)
    self.setLayout(self.layout)

    self.update_timer = QtCore.QTimer()
    self.update_timer.timeout.connect(self.graph.update)
    self.update_timer.setInterval(interval)

  def start(self):
    self.update_timer.start()

  def set_interval(self, interval):
    self.update_timer.setInterval(interval)

  def add_data_point(self, name, t, y):
    self.graph.add_data_point(name, t, y)

  def add_data_set(self, name, t, y):
    self.graph.add_data_set(name, t, y)

  def add_line(self, name, color=None, downsample=None):
    self.graph.add_line(name, color=color, downsample=downsample)

  def remove_line(self, name):
    self.graph.remove_line(name)

  def hide_line(self, name):
    self.graph.hide_line(name)

  def show_line(self, name):
    self.graph.show_line(name)

  def run_test(self, interval=50, dynamic=False, freqs=[1]):
    if dynamic:
      self.test_waves = []
      n = 0

      for f in freqs:
        self.test_waves.append(f)
        n += 1
        self.add_line(f, color=QtGui.QPen(QtGui.QColor(2**n, 2**(n+1), 2**(n+2))))

      self.t = 0
      self.dt = (interval/1000.0)
      self.set_interval(interval)

      self.data_timer = QtCore.QTimer()
      self.data_timer.timeout.connect(self._dynamic_update)
      self.data_timer.setInterval(interval)

      self.data_timer.start()
      self.update_timer.start()

    else:

      t = np.linspace(0, 1, 1000)
      f = freqs[0]
      for n in range(1, 6):
        self.add_line(n, color=QtGui.QPen(QtGui.QColor(2**n, 2**(n+1), 2**(n+2))))
        y = np.sin(2*np.pi*n*f*t)
        self.add_data_set(n, t, y)
      self.graph.update()

  def _dynamic_update(self):
    self.t += self.dt
    for f in self.test_waves:
      ys = np.sin(2*np.pi*f*self.t)
      self.add_data_point(f, self.t, ys)

class TimeSeriesController(QtGui.QWidget):
  def __init__(self):
    self.controllers = []

  def add_controller(self, name):
    pass
    # self.controllers.append()


class LineGraph(pg.PlotWidget):
  def __init__(self, name=None, maxlen=1000, ylim=[-1 , 1]):
    super(LineGraph, self).__init__(name=name)

    self.maxlen = maxlen
    self.lines = dict()

    self.showGrid(x=True, y=True)
    self.legend = self.addLegend()

  def set_ylim(self, ylim):
    self.setYRange(ylim[0], ylim[1])

  def add_data_point(self, name, t, y):
    self.lines[name][1].append([t, y])

  def add_data_set(self, name, t, y):
    self.lines[name][1].extend(zip(t, y))

  def add_line(self, name, color=None, downsample=None):
    artist = self.plot(pen=color, downsample=downsample)
    self.legend.addItem(artist, name)
    self.lines[name] = (artist, deque(maxlen=self.maxlen))

  def remove_line(self, name):
    self.removeItem(self.lines[name][0])
    self.legend.removeItem(name)
    del self.lines[name]

  def hide_line(self, name):
    self.removeItem(self.lines[name][0])
    self.legend.removeItem(name)

  def show_line(self, name):
    self.add_item(self.lines[name][0])

  def update(self):
    for k in self.lines.keys():
      artist = self.lines[k][0]
      data = np.array(self.lines[k][1])
      if data.size > 2:
        artist.setData(x=data[:,0], y=data[:,1])


if __name__ == "__main__":
  # Create the App
  import sys
  app = QtGui.QApplication(sys.argv)
  time_series = TimeSeries(interval=50, maxlen=100)

  time_series.run_test( interval=50, dynamic=True, freqs=[.1, .2, .3])
  time_series.show()
  sys.exit(app.exec_())
