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
# @Last Modified time: 2015-01-21 11:28:33
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
from collections import deque

  # def add_controller(self):
  #   self.controller = PointSeriesController(self.line_names.keys(), self._controller_callback)
  #   self.layout.addWidget(self.controller)

class Graph(pg.PlotWidget):
  def __init__(self, **kwargs):
    super(Graph, self).__init__(**kwargs)
    self.showGrid(x=True, y=True)
    if kwargs['legend']:
      self.legend = self.addLegend()

  def add_data(self, data, **kwargs):
    # if not isinstance(data, numpy.ndarray)
    for n in kwargs["names"]:
      if n in sorted(self.plots.keys()):
        if max(data.shape) > 1:
          self.plots[n].extend(data)
        else:
          self.plots[n].append(data)
      else:
        self.add_plot()

  def add_plot(self, name, maxlen, **kwargs):
    self.artists[name] = self.plot(**kwargs)
    self.plots[name] = deque(maxlen=maxlen)
    self.legend.addItem(artist, name)

  def remove_plot(self, name):
    self.removeItem(self.plot[name][0])
    self.legend.removeItem(name)

    del self.plot[name]


  def hide_line(self, name):
    self.legend.removeItem(name)
    self.removeItem(self.lines[name][0])

  def show_line(self, name):
    self.addItem(self.lines[name][0])
    self.legend.addItem(self.lines[name][0], name)

  def update(self):
    for k in sorted(self.lines.keys()):
      artist = self.lines[k][0]
      data = np.array(self.lines[k][1])
      if data.size > 2:
        artist.setData(x=data[:, 0], y=data[:, 1])

  # class LineGraph(pg.PlotWidget):
  # def __init__(self, name=None, maxlen=1000, ylim=[-1 , 1]):
  #   super(LineGraph, self).__init__(name=name)

  #   self.maxlen = maxlen
  #   self.lines = dict()



  # def set_ylim(self, ylim):
  #   self.setYRange(ylim[0], ylim[1])


