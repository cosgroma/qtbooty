#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   cosgrma
# @Last Modified time: 2015-12-04 04:54:50

import sys

from QtBooty import App
from QtBooty import framework


def change(param, changes):
  print("tree changes:")
  for param, change, data in changes:
    # path = p.childPath(param)
    # if path is not None:
    #   childName = '.'.join(path)
    # else:
    childName = param.name()
    print('  parameter: %s' % childName)
    print('  change:    %s' % change)
    print('  data:      %s' % str(data))
    print('  ----------')


app = App()
io_grid = framework.IOGrid()
p, ioconfig = io_grid.load_config_file('io_grid_test5.json')
io_grid.connect_changed_callback(change)
app.add_widget(io_grid)
app.run()
