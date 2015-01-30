#!/usr/bin/env python
# -*- coding: utf-8 -*-;
"""Name of module.

Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
  Examples can be given using either the ``Example`` or ``Examples``
  sections. Sections support any reStructuredText formatting, including
  literal blocks::

      $ python surf.py

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
# @Date:   2014-12-30 05:25:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-28 06:11:47
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
# from collections import deque

# try:
#   from PySide import QtGui, QtCore
#   backend = 'pyside'
# except ImportError:
from PyQt4 import QtGui, QtCore

front_end = 'visvis'
# front_end = 'matplotlib'

from QtBooty.graphs import MplCanvas, VisSurface, GraphUpdater


class Surface(QtGui.QWidget):
  def __init__(self, name=None, controller=False):
    super(Surface, self).__init__()
    self.layout = QtGui.QHBoxLayout()

    if front_end == "visvis":
      self.graph = VisSurface(self)
    else:
      self.graph = MplCanvas(self, "surface")

    self.layout.addWidget(self.graph)
    self.setLayout(self.layout)

  def set_lims(self, xlim, ylim, zlim):
    self.graph.set_lims(xlim, ylim, zlim)

  def set_xymesh(self, x, y):
    self.graph.set_xymesh(x, y)

  def set_boundary(self, x_r, y_r, z_r):
    self.graph.set_boundary(x_r, y_r, z_r)

  def update(self, data, config):
    self.graph.set_data(data[-1])
    self.graph.update_plot()


if __name__ == '__main__':
  # Create the App
  import sys
  app = QtGui.QApplication(sys.argv)
  surf = Surface(interval=3000)

  X = np.arange(511, 513, 0.5)
  Y = np.arange(-700, 700, 100)
  Z = np.arange(0, 10e3, 1e3)

  xlim = (np.min(X), np.max(X))
  ylim = (np.min(Y), np.max(Y))
  zlim = (np.min(Z), np.max(Z))

  # X = np.arange(0, 1023, 0.5)
  # Y = np.arange(-7000, 7000, 1000)
  # Z = np.arange(0, 10e6, 1e6)

  # X = np.arange(-5, 5, 1)
  # Y = np.arange(-5, 5, 1)
  # Z = np.arange(0, 10, 1)

  # surf.set_boundary(X, Y, Z)
  surf.set_xymesh(X, Y)
  surf.set_lims(xlim, ylim, zlim)
  X, Y = np.meshgrid(X, Y)
  surf.add_data(np.abs(np.random.normal(0, Z.ptp()/10.0, size=X.shape)))
  surf._update()
  surf.start()
  surf.show()
  sys.exit(app.exec_())
