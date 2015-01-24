#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python graph_updater.py

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
# @Date:   2014-12-30 14:23:04
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-23 10:56:25
# REF: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google
# REF: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

__author__ = "Mathew Cosgrove"
__copyright__ = ""
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Mathew Cosgrove"
__email__ = "mathew.cosgrove@ngc.com"
__status__ = "Development"

import numpy as np
from PyQt4 import QtGui, QtCore
from collections import deque

from QtBooty import App


class GraphScheduler(object):
  """docstring for GraphScheduler"""
  def __init__(self):
    super(GraphScheduler, self).__init__()
    self.updaters = []

  def add_graph(self, graph, **kwargs):
    updater = GraphUpdater(graph, **kwargs)
    self.updaters.append(updater)
    return updater

  def remove_graph(self, graph):
    self.updaters.remove(graph)

  def get_statistics(self, graph):
    pass

  def start(self):
    # spawn graph monitor

    # Start all of the  updaters
    for updater in self.updaters:
      updater.start()

  def stop(self):
    # stop graph monitor
    # Stop all the updaters
    for updater in self.updaters:
      updater.stop()




class GraphUpdater(object):
  """docstring for GraphUpdater"""
  def __init__(self, graph, maxlen=1000, interval=1000):
    super(GraphUpdater, self).__init__()

    self.graph = graph
    self.maxlen = maxlen
    self.interval = interval
    # self.setup()
    self.setup_update_timers()
    self.config = dict()

    self.on_update = None
    self.data = None

  def setup_update_timers(self):
    self.update_timer = QtCore.QTimer()
    self.update_timer.timeout.connect(self._update)
    self.update_timer.setInterval(self.interval)

  def get_interval(self):
    return self.inteval

  def set_interval(self, interval):
    self.interval = interval
    self.update_timer.setInterval(interval)

  def get_maxlen(self):
    return self.maxlen

  def set_maxlen(self, maxlen):
    self.maxlen = maxlen
    self.data = deque(maxlen=self.maxlen)

  def add_data(self, data, config):
    if self.data is None:
      self.data = deque(maxlen=self.maxlen)
    self.config.update(config)
    self.data.append(data)

  def set_update_callback(self, callback):
    self.on_update = callback

  def start(self):
    self.update_timer.start()

  def stop(self):
    self.update_timer.stop()

  def _update(self):
    dmat = np.concatenate(self.data, axis=1)
    self.graph.update(dmat.transpose(), self.config)




# # app = App('../config/app_config.json')
# t = np.linspace(0, 1, 8, endpoint=False)
# # t = np.array([1])
# r1 = np.random.randn(len(t))
# r2 = np.random.randn(len(t))
# npm = np.matrix([t, r1, r2])
# data = deque(maxlen=10)
# data.append(npm)
# t += 1
# npm = np.matrix([t, r1, r2])
# data.append(npm)
# dmat = np.concatenate(data, axis=1)
# print dmat.shape
# print dmat[:,]

# npa = np.array(range(0,10))
# # print dmat

# print npa.shape



# def main():



# if __name__ == '__main__':
#   main()