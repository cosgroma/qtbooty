#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 22:27:47
# @Last Modified by:   cosgrma
# @Last Modified time: 2015-08-05 07:37:07

import pyqtgraph as pg
from PyQt4 import QtGui, QtCore, Qt
# from pyqtgraph.Qt import QtCore, QtGui
# from PyQt4 import QtCore, QtGui, Qt
pg.setConfigOption('background', (50, 50, 50))
pg.setConfigOption('foreground', 'w')
from collections import deque
import numpy as np

import random as r
from QtBooty.framework import IOGrid


class PointSeries(QtGui.QWidget):

  def __init__(self, name=None, controller=False, interval=1000, maxlen=1000, ylim=[-1, 1], setlegend=True):
    super(PointSeries, self).__init__()
    self.maxlen = maxlen
    self.interval = interval
    self.ylim = ylim

    self.line_names = dict()

    self.layout = QtGui.QHBoxLayout()
    self.graph = LineGraph(name=name, maxlen=maxlen, setlegend=setlegend)

    if ylim is not None:
      self.graph.set_ylim(self.ylim)

    self.layout.addWidget(self.graph)
    self.setLayout(self.layout)

    self.update_timer = QtCore.QTimer()
    self.update_timer.timeout.connect(self.graph.update)
    self.update_timer.setInterval(interval)

  def start(self):
    self.update_timer.start()

  def set_maxlen(self, maxlen):
    self.graph.set_maxlen(maxlen)
    self.maxlen = maxlen

  def set_interval(self, interval):
    self.update_timer.setInterval(interval)

  def add_data_point(self, name, x, y):
    self.graph.add_data_point(name, x, y)

  def add_data_set(self, name, x, y):
    self.graph.add_data_set(name, x, y)

  def add_line(self, name, color=None, downsample=None):
    self.graph.add_line(name, color=color, downsample=downsample)
    self.line_names[name] = False

  def remove_line(self, name):
    self.graph.remove_line(name)
    del self.line_names[name]

  def hide_line(self, name):
    self.graph.hide_line(name)
    self.line_names[name] = False

  def show_line(self, name):
    self.graph.show_line(name)
    self.line_names[name] = True

  def add_controller(self):
    self.controller = PointSeriesController(self.line_names.keys(), self._controller_callback)
    self.layout.addWidget(self.controller)

  def _controller_callback(self, args):
    pyobj = args[0]
    name = args[1]
    if self.line_names[name]:
      self.hide_line(name)
    else:
      self.show_line(name)

  def run_test(self, interval=50, dynamic=False, freqs=[1]):
    if dynamic:
      self.test_waves = []
      self.n = 0
      self.freqs = freqs
      for f in freqs:
        self.test_waves.append(f)
        self.n += 1
        self.add_line(f, color=QtGui.QPen(QtGui.QColor(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))))

      self.t = 0
      self.dt = (interval / 1000.0)
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
        self.add_line(n, color=QtGui.QPen(QtGui.QColor(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))))
        y = np.sin(2 * np.pi * n * f * t)
        self.add_data_set(n, t, y)
      self.graph.update()

  def _dynamic_update(self):
    self.t += self.dt
    for f in self.test_waves:
      ys = np.sin(2 * np.pi * f * self.t)
      self.add_data_point(f, self.t, ys)

    if self.t % 5 < 2 * self.dt:
      self.n += 1

      f = self.freqs[-1] + self.freqs[0]
      self.freqs.append(f)
      self.test_waves.append(f)
      self.controller.io_config["groups"][0]["items"].append({
          "class": "button",
          "qtype": "check",
          "label": str(f),
          "name": "check_" + str(f),
          "clicked": self._controller_callback,
          "args": [f]
      })
      self.controller.io_grid.config_update(self.controller.io_config)
      self.add_line(f, color=QtGui.QPen(QtGui.QColor(r.randint(0, 64), r.randint(0, 64) * 2, r.randint(0, 64) * 4)))


class PointSeriesController(QtGui.QWidget):

  def __init__(self, line_names, callback):
    super(PointSeriesController, self).__init__()
    self.layout = QtGui.QHBoxLayout()
    self.setLayout(self.layout)
    self.io_grid = IOGrid()

    io_config_layout = {
        "layout": ["v", "na"],
        "groups": [{
            "enabled": True,
            "box_enabled": True,
            "group_name": "Plot Control",
            "layout": ["v", "t"],
            "items": []
        }]
    }
    # def add_line_controllers(self, line_names):
    for n in line_names:
      io_config_layout["groups"][0]["items"].append({
          "class": "button",
          "qtype": "check",
          "label": str(n),
          "name": "check_" + str(n),
          "clicked": callback,
          "args": [n]
      })
    self.params, self.io_config = self.io_grid.load_config(io_config_layout)
    self.layout.addWidget(self.io_grid)

  def onChange(self, param, changes):
    pass


class LineGraph(pg.PlotWidget):

  def __init__(self, name=None, maxlen=1000, ylim=[-1, 1], setlegend=True):
    super(LineGraph, self).__init__(name=name)

    self.maxlen = maxlen
    self.lines = dict()
    self.setlegend = setlegend
    self.showGrid(x=True, y=True)
    if self.setlegend:
      self.legend = self.addLegend()

    self.setSizePolicy(
        QtGui.QSizePolicy(
            QtGui.QSizePolicy.MinimumExpanding,
            QtGui.QSizePolicy.MinimumExpanding
        )
    )

  def set_maxlen(self, maxlen):
    self.maxlen = maxlen
    temp = dict()
    for k in self.lines.keys():
      artist = self.lines[k][0]
      temp[k] = (artist, deque(maxlen=self.maxlen))
    self.lines = temp

  def set_ylim(self, ylim):
    self.setYRange(ylim[0], ylim[1])

  def add_data_point(self, name, x, y):
    self.lines[name][1].append([x, y])

  def add_data_set(self, name, x, y):
    self.lines[name][1].extend(zip(x, y))

  def add_line(self, name, color=None, downsample=None):
    if name in self.lines.keys():
      return
    artist = self.plot(pen=color, downsample=downsample)
    self.legend.addItem(artist, name)
    self.lines[name] = (artist, deque(maxlen=self.maxlen))
    self.hide_line(name)

  def remove_line(self, name):
    self.removeItem(self.lines[name][0])
    self.legend.removeItem(name)
    del self.lines[name]

  def hide_line(self, name):
    self.legend.removeItem(name)
    self.removeItem(self.lines[name][0])

  def show_line(self, name):
    self.addItem(self.lines[name][0])
    self.legend.addItem(self.lines[name][0], name)

  def update(self):
    for k in self.lines.keys():
      artist = self.lines[k][0]
      data = np.array(self.lines[k][1])
      if data.size > 2:
        artist.setData(x=data[:, 0], y=data[:, 1])


if __name__ == "__main__":
  # Create the App
  import sys
  app = QtGui.QApplication(sys.argv)
  time_series = PointSeries(interval=50, maxlen=100)
  time_series.run_test(interval=50, dynamic=True, freqs=[.1, .2, .3])
  time_series.add_controller()
  time_series.show()
  sys.exit(app.exec_())
