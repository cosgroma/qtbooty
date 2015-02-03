#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-02-02 23:48:02

import sys

from QtBooty import App
from QtBooty import framework

app = App()
io_grid = framework.IOGrid()
p = io_grid.load_config_file('../config/io_grid.json')


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
io_grid.connect_changed_callback(change)
app.add_widget(io_grid)
app.run()
