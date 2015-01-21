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
# @Last Modified by:   mac
# @Last Modified time: 2014-12-30 14:56:05
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

class GraphUpdater(QtGui.QWidget):
  """docstring for GraphUpdater"""
  def __init__(self, interval=1000, maxlen=100):
    super(GraphUpdater, self).__init__()
    # self.arg = arg
    self.maxlen = maxlen
    self.interval = interval
    self.data = dict()

    self.setup()
    self.setup_update_timers()

  def setup(self):
    self.layout = QtGui.QHBoxLayout()
    size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
    self.setSizePolicy(size_policy)
    self.setLayout(self.layout)

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

  def new_deque(self, name):
    self.data[name] = deque(maxlen=self.maxlen)
    return self.data[name]

  def start(self):
    self.update_timer.start()

  def stop(self):
    self.update_timer.stop()

  def _update(self):
    pass