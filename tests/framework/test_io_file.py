#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-02-07 13:21:10

import sys

from QtBooty import App
from QtBooty import framework

## If anything changes in the tree, print a message
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

# p.sigTreeStateChanged.connect(change)

app = App()
tabs = framework.Tabs()
io_grid = framework.IOGrid()
io_grid1 = framework.IOGrid()
io_grid2 = framework.IOGrid()

p = io_grid.load_config_file('io_grid.json')
p1 = io_grid1.load_config_file('io_grid_test2.json')
p2 = io_grid2.load_config_file('io_grid_test3.json')

io_grid.connect_changed_callback(change)
io_grid1.connect_changed_callback(change)
io_grid2.connect_changed_callback(change)

tabs.add_tab(io_grid, "IO Grid")
tabs.add_tab(io_grid1, "IO Grid 1")
tabs.add_tab(io_grid2, "IO Grid 3")
app.add_widget(tabs)
app.run()
