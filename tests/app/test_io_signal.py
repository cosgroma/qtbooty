#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-21 23:46:14

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

groups = [dict()]*5
for i in range(0, 5):
  groups[i]["box_enabled"] = True
  groups[i]["box_name"] = "signal::controller"
  groups[i]["layout"] = ["v", "na"]
  groups[i]["items"] = [{
   "class": "slider",
   "config": {
     "label": "Power",
     "display": True,
     "orientation": "v",
     #"policy": "smart",
     "valueChanged": slider_callback,
     "args": ["dB"]
   }
 }, {
   "class": "slider",
   "config": {
     "type": "dial",
     "label": "Doppler",
     "display": True,
     "orientation": "v",
     "range": [-5e3, 5e3],
     #"policy": "smart",
     "valueChanged": slider_callback,
     "args": ["Hz"]
   }
 }
]



# , {
#       "class": "slider",
#       "config": {
#         "type": "dial",
#         "label": "Doppler",
#         "display": True,
#         "orientation": "v",
#         "range": [-5e3, 5e3],
#         #"policy": "smart",
#         "valueChanged": slider_callback,
#         "args": ["Hz"]
#       }
#     }

io_grid = framework.IOGrid()

config = io_grid.config_init(len(groups), [len(g["items"]) for g in groups])

config["layout"] = ["h", "j"]
[d.update(u) for d, u in zip(config["groups"], groups)]

# import json
# print config

io_grid.config_widget(config)
app.add_widget(io_grid)
app.run()


