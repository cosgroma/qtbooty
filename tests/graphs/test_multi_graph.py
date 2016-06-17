#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2016-06-16 23:52:30

import sys
import os
sys.path.append(os.path.dirname(os.path.join(os.path.dirname(__file__), "../../qtbooty")))
# sys.path.append('/home/cosgroma/workspace/sergeant/guis')

from qtbooty import App
from qtbooty import graph
from collections import deque
import numpy as np

app = App('../config/app_config.json')
magnitude_plot = graph.Line(legend=False, controller=False)
phase_plot = graph.Line(legend=False, controller=False)

# gscheduler = graphs.GraphScheduler()
# mag_updater = gscheduler.add_graph(magnitude_plot, maxlen=1000, interval=50)


def update():
  pass


# update.config = {
#   "plots":[{
#     "name": "cosine",
#     "plot kwargs": {
#       "pen": 'r',
#       "downsample": None,
#       "fillLevel": 0,
#       "brush": (0, 0, 255, 80)
#     }
#   },{
#     "name": "sine",
#     "plot kwargs": {
#       "pen": 'b',
#       "downsample": None
#     }
#   }]
# }


app.add_widget(magnitude_plot)
app.add_widget(phase_plot)
# app.add_timer(update.intr, update)
# gscheduler.start()
app.run()
