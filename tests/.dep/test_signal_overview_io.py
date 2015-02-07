#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-30 00:17:34

import sys
sys.path.append('/home/cosgroma/workspace/libs/python/modules')

from QtBooty import App
from QtBooty import framework

app = App()

io_grid = framework.IOGrid()

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

groups[0]["box_enabled"] = False
groups[0]["box_name"] = "consellation::controller"
groups[0]["scrollable"] = True
groups[0]["layout"] = ["h", "c"]

def slider_callback(args):
  print "got callback"

groups[0]["items"] = []
for i in range(0, 12):
  groups[0]["items"].append(
    {
      "class": "slider",
      "config": {
        "label": "slider%d" % i,
        "display": True,
        "orientation": "v",
        # "policy": "smart",
        "valueChanged": slider_callback,
        "args": ["dB"]
      }
    }
  )


config = io_grid.config_init(len(groups), [len(g["items"]) for g in groups])

config["layout"] = ["v", "c"]
[d.update(u) for d, u in zip(config["groups"], groups)]
# config["groups"].update(groups)

io_grid.config_widget(config)
app.add_widget(io_grid)
app.run()


