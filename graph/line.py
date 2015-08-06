#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python line.py

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
# @Last Modified by:   cosgrma
# @Last Modified time: 2015-07-29 08:36:11
# REF: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google
# REF: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "cosgroma@gmail.com"
__status__ = "Development"


import pyqtgraph as pg
pg.setConfigOption('background', (50, 50, 50))
pg.setConfigOption('foreground', 'w')
from PyQt4 import QtGui

import numpy as np
from QtBooty.framework import IOGrid


def rpen():
  return QtGui.QPen(
      QtGui.QColor(
          np.random.randint(255),
          np.random.randint(255),
          np.random.randint(255)))


class Line(QtGui.QWidget):

  def __init__(self, legend=False, controller=False, update_controller=False, size=(1, 0), title=None, range=None):
    super(Line, self).__init__()

    self.artists = dict()

    self.layout = QtGui.QHBoxLayout()

    self.setup_graph(legend=legend, range=range)
    self.layout.addWidget(self.graph)

    self.controller_enabled = controller
    # self.setSizePolicy(
    #     QtGui.QSizePolicy(
    #         QtGui.QSizePolicy.MinimumExpanding,
    #         QtGui.QSizePolicy.MinimumExpanding
    #     )
    # )
    self.setLayout(self.layout)
    # self.setMaximumWidth(1200)
    if self.controller_enabled:
      # self.setup_controller()
      self.layout.addWidget(self.controller)

  def setup_graph(self, legend=False, range=None):
    self.graph = pg.PlotWidget()
    if range is not None:
      if range['y_range'] != "auto":
        self.graph.setYRange(*range['y_range'])
      if range['x_range'] != "auto":
        self.graph.setYRange(*range['x_range'])

    # self.graph.setSizePolicy(
    #     QtGui.QSizePolicy(
    #         QtGui.QSizePolicy.MinimumExpanding,
    #         QtGui.QSizePolicy.MinimumExpanding
    #     )
    # )
    # self.graph.setMaximumWidth(1000)
    self.legend_enabled = False
    self.graph.showGrid(x=True, y=True)

    if legend:
      self.legend = self.graph.addLegend()
      self.legend_enabled = True

  def setup_controller(self):
    self.controller = IOGrid()
    self.controller.load_config()
    # self.controller_config = self.controller.config_init(1, [0])
    # self.controller_config["groups"][0]["box_enabled"] = True
    # self.controller_config["groups"][0]["box_name"] = "plot control"
    # self.controller_config["groups"][0]["checkable"] = False
    # self.controller_config["groups"][0]["layout"] = ["v", "t"]
    # self.controller.config_widget(self.controller_config)
    # print self.controller_config

  def link_xaxis(self, graph):
    self.graph.getViewBox().setXLink(graph.getViewBox())

  def controller_callback(self, args):
    button = args[0]
    name = args[1]
    if not button.isChecked():
      # print "diable:", name
      self.hide_line(name)
    else:
      self.show_line(name)

  def add_plot(self, name, plot_args):

    self.artists[name] = self.graph.plot(**plot_args)
    if self.legend_enabled:
      self.legend.addItem(self.artists[name], name)

    if self.controller_enabled:
      self.controller_config["groups"][0]["items"].append({
          "class": "button",
          "added": False,
          "name": str(name),
          "qtype": "check",
          "label": str(name),
          "clicked": self.controller_callback,
          "enabled": True,
          "args": [name]
      })
      self.controller.config_update(self.controller_config)

  def remove_plot(self, name):
    self.graph.removeItem(self.artists[name])
    if self.legend_enabled:
      self.legend.removeItem(name)

  def hide_line(self, name):
    self.legend.removeItem(name)
    self.graph.removeItem(self.artists[name])

  def show_line(self, name):
    self.graph.addItem(self.artists[name])
    self.legend.addItem(self.artists[name], name)

  def update(self, data, config):
    """
    @summary: Updates
    @param data:
    @param config:
    @result:
    """
    # Cycle through the plot config and add the data to the artist
    for idx, plot in enumerate(config['plots'], start=1):
      # If the plot does not exsist add it
      if plot["name"] not in self.artists.keys():
        self.add_plot(plot["name"], plot["plot kwargs"])
      # Update the line artist with the new data
      self.artists[plot["name"]].setData(
          x=np.squeeze(np.asarray(data[:, 0])),
          y=np.squeeze(np.asarray(data[:, idx])))


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

  # def add_controller(self):
  #   self.controller = PointSeriesController(self.line_names.keys(), self._controller_callback)
  #   self.layout.addWidget(self.controller)
