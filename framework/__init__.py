#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-22 22:43:41
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-02-07 08:17:19

backend = "pyqtgraph"

if backend == "pyqtgraph":
  from pyqtgraph.Qt import QtGui, QtCore


from tabs import Tabs
from io_grid import IOGrid