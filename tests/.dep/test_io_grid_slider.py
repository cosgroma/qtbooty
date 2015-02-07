#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-21 20:07:52

import sys
sys.path.append('/Users/cosgroma/workspace')

from QtBooty import App
from QtBooty import framework

app = App()



groups = [dict()]

# slider_defaults = {
#   "type":         "default",
#   "label":        "",
#   "position":     "above",
#   "range":        [0, 100],
#   "orientation":  "h",
#   "policy":       "expand",
#   "display":      False,
#   "valueChanged": None,
#   "args":         [None]
# }

def slider_callback(args):
  print "got callback"

groups[0]["box_enabled"] = False
groups[0]["box_name"] = "class::slider"
groups[0]["layout"] = ["v", "na"]

groups[0]["items"] = [
  {
    "class": "slider",
    "config": {
      "label": "slider0",
      "display": True,
      "orientation": "v",
      #"policy": "smart",
      "valueChanged": slider_callback,
      "args": ["dB"]
    }
  }
]

io_grid = framework.IOGrid()

config = io_grid.config_init(len(groups), [len(g["items"]) for g in groups])

config["layout"] = ["v", "j"]
[d.update(u) for d, u in zip(config["groups"], groups)]

# import json
# print config

io_grid.config_widget(config)
app.add_widget(io_grid)
app.run()


