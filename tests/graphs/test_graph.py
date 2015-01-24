#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-23 11:03:55

import sys
# sys.path.append('/home/cosgroma/workspace/sergeant/guis')

from QtBooty import App
from QtBooty import graphs
from collections import deque
import numpy as np

app = App('../config/app_config.json')
time_series = graphs.Line(legend=True)

gscheduler = graphs.GraphScheduler()
ts_updater = gscheduler.add_graph(time_series, maxlen=1000, interval=50)

def update():
  npm = np.matrix([
    update.t,
    10*np.cos(2*np.pi*.3*update.t),
    10*np.sin(2*np.pi*.6*update.t)
  ])
  ts_updater.add_data(npm, update.config)
  update.t += update.intr/1000.0

update.intr = 10.0
# update.t = np.array([0.0])
update.t = np.linspace(0, update.intr/1000.0, 10, endpoint=False)

update.config = {
  "plots":[{
    "name": "cosine",
    "plot kwargs": {
      "pen": 'r',
      "downsample": None,
      "fillLevel": 0,
      "brush": (0, 0, 255, 80)
    }
  },{
    "name": "sine",
    "plot kwargs": {
      "pen": 'b',
      "downsample": None
    }
  }]
}

# ,{
#     "name": "square",
#     "plot kwargs": {
#       "pen": 'g',
#       "downsample": None
#     }
#   }

app.add_widget(time_series)
app.add_timer(update.intr, update)
gscheduler.start()
app.run()



# app = App('../config/app_config.json')

# npa = np.array(range(0, 10))
# print dmat
# gu = graphs.GraphUpdater()
# gu.add_data(npa, ["npa"])

# print gu.data["npa"]

# graph = graphs.Graph(legend=False)

# app.add_widget(graph)
# app.run()
