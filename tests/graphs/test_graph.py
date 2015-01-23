#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-23 00:53:11

import sys
# sys.path.append('/home/cosgroma/workspace/sergeant/guis')

from QtBooty import App
from QtBooty import graphs
from collections import deque
import numpy as np

t = np.linspace(0, 1, 10, endpoint=False)

app = App('../config/app_config.json')
time_series = graphs.Graph(maxlen=5000, legend=True)

# def cn(n):
#    c = np.exp(-1j*2*n*np.pi*time/period)
#    return c.sum()/c.size

# def f(x, Nh):
#    f = np.array([2*cn(i)*np.exp(1j*2*i*np.pi*x/period) for i in range(1, Nh+1)])
#    return f.sum()

# datafun = lambda t: np.array([f(t,50).real])

def update():
  npm = np.matrix([
    update.t,
    10*np.cos(2*np.pi*.3*update.t),
    10*np.sin(2*np.pi*.6*update.t)
  ])
  time_series.add_data(npm, update.config)
  update.t += update.intr/1000.0

update.intr = 10.0
# update.t = np.array([0.0])
update.t = np.linspace(0, update.intr/1000.0, 100, endpoint=False)

update.config = {
  "plots":[{
    "name": "cosine",
    "plot kwargs": {
      "pen": 'r',
      "downsample": None
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
time_series.set_interval(100)
time_series.start()
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
