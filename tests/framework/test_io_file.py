#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2016-06-17 00:00:04

import sys
import os
sys.path.append(os.path.dirname(os.path.join(os.path.dirname(__file__), "../../qtbooty")))

from qtbooty import App
from qtbooty import framework

# If anything changes in the tree, print a message


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
io_grid3 = framework.IOGrid()
io_grid4 = framework.IOGrid()
config5 = {
    "layout": ["h", "na"],
    "groups": [{
        "enabled": True,
        "box_enabled": True,
        "group_name": "data selection",
        "layout": ["v", "t"],
        "items": [{
            "class": "button",
            "name": "power0",
            "qtype": "radio"
        }]
    }]
}

radio_button = {
    "class": "button",
    "name": "power1",
    "qtype": "radio"
}


p, ioconfig = io_grid.load_config_file('io_grid.json')
p1, ioconfig1 = io_grid1.load_config_file('io_grid_test2.json')
p2, ioconfig2 = io_grid2.load_config_file('io_grid_test3.json')
p3, ioconfig3 = io_grid3.load_config_file('io_grid_test4.json')
p4, ioconfig4 = io_grid4.load_config(config5)

io_grid.connect_changed_callback(change)
io_grid1.connect_changed_callback(change)
io_grid2.connect_changed_callback(change)
io_grid3.connect_changed_callback(change)
io_grid4.connect_changed_callback(change)

tabs.add_tab(io_grid, "IO Grid")
tabs.add_tab(io_grid1, "IO Grid 1")
tabs.add_tab(io_grid2, "IO Grid 3")
tabs.add_tab(io_grid3, "IO Grid 4")
tabs.add_tab(io_grid4, "IO Grid 5")
app.add_widget(tabs)


ioconfig4["groups"][0]["items"].append(radio_button)
print ioconfig4
io_grid4.config_update(ioconfig4)
# radio_button


app.run()
