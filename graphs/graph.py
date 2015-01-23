#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python graph.py

Section breaks are created by simply resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
  module_level_variable (int): Module level variables may be documented in
    either the ``Attributes`` section of the module docstring, or in an
    inline docstring immediately following the variable.

    Either form is acceptable, but the two should not be mixed. Choose
    one convention to document module level variables and be consistent
    with it.

.. _Google Python Style Guide:
   http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

"""
# @Author: Mathew Cosgrove
# @Date:   2015-01-14 01:09:36
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-23 01:41:38
# REF: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google
# REF: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "cosgroma@gmail.com"
__status__ = "Development"

import numpy as np
import pyqtgraph as pg
from PyQt4 import QtGui
from QtBooty.framework import IOGrid
from graph_updater import GraphUpdater
  # def add_controller(self):
  #   self.controller = PointSeriesController(self.line_names.keys(), self._controller_callback)
  #   self.layout.addWidget(self.controller)

# class LineController(QtGui.QWidget):
#   def __init__(self, graph):
#     super(LineController, self).__init__()
#     self.graph = graph
#     self.layout = QtGui.QHBoxLayout()
#     self.setLayout(self.layout)
#     self.io_grid = IOGrid()
#     self.line_names = self.graph.get_names()
#     self.config = self.io_grid.config_init(1, [len(self.line_names)])

#     self.config["groups"][0]["box_enabled"] = True
#     self.config["groups"][0]["box_name"] = "plot control"
#     self.config["groups"][0]["layout"] = ["v", "t"]

#   # def add_line_controllers(self, line_names):
#     for n in line_names:
#       self.config["groups"][0]["items"].append({
#           "class": "button",
#           "config": {
#             "type": "check",
#             "label": str(n),
#             "clicked": callback,
#             "args": n
#             }
#         })
#     # self.controllers = []
#     self.io_grid.config_widget(self.config)
#     self.layout.addWidget(self.io_grid)

class Line(pg.PlotWidget):
  def __init__(self, maxlen=1000, legend=False):
    super(Line, self).__init__()
    self.set_maxlen(maxlen)
    self.legend_enabled = False
    self.showGrid(x=True, y=True)

    if legend:
      self.legend = self.addLegend()
      self.legend_enabled = True

    self.artists = dict()

  def update(self, data, config):
    data = data.transpose()
    for idx, plot in enumerate(config['plots'], start=1):
      if plot["name"] not in self.artists.keys():
        self.add_plot(plot["name"], plot["plot kwargs"])

      self.artists[plot["name"]].setData(
        x=np.squeeze(np.asarray(data[:, 0])),
        y=np.squeeze(np.asarray(data[:, idx])))
      cnt += 1

  def add_plot(self, name, plot_args):
    self.artists[name] = self.plot(**plot_args)

    self.legend.addItem(self.artists[name], name) if self.legend_enabled

# def remove_plot(self, name):
#   self.removeItem(self.plot[name][0])
#   self.legend.removeItem(name)

#   del self.plot[name]


# def hide_line(self, name):
#   self.legend.removeItem(name)
#   self.removeItem(self.lines[name][0])

# def show_line(self, name):
#   self.addItem(self.lines[name][0])
#   self.legend.addItem(self.lines[name][0], name)

# def update(self):
#   for k in sorted(self.lines.keys()):
#     artist = self.lines[k][0]
#     data = np.array(self.lines[k][1])
#     if data.size > 2:
#       artist.setData(x=data[:, 0], y=data[:, 1])

# class LineLine(pg.PlotWidget):
# def __init__(self, name=None, maxlen=1000, ylim=[-1 , 1]):
#   super(LineGraph, self).__init__(name=name)

#   self.maxlen = maxlen
#   self.lines = dict()

# def set_ylim(self, ylim):
#   self.setYRange(ylim[0], ylim[1])


