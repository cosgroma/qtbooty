#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-22 19:56:35

import sys
# sys.path.append('/home/cosgroma/workspace/sergeant/guis')

from QtBooty import App
from QtBooty import graphs
from collections import deque
import numpy as np

app = App('../config/app_config.json')
time_series = graphs.Graph()

datafun = lambda t: 10*np.cos(2*np.pi*.3*t) + np.random.randn(len(t))

def update():
  time_series.add_data(
    np.matrix(
      update.t,
      update.func(update.t)
    ),
    update.config
  )

  update.t += (update.intr/1000.0)

update.config = {
  "names": ["cosine"],
  "plot kwargs": {
    "color": 'r'
  }
}

update.t = np.array([0])
update.intr = 10
update.func = datafun

app.add_widget(time_series)
app.add_timer(update.intr, update)
time_series.set_interval(500)
time_series.start()
app.run()



# # app = App('../config/app_config.json')
# t = np.linspace(0, 1, 1, endpoint=False)
# # t = np.array([1])
# data = deque(maxlen=10)
# # r1 = np.random.randn(len(t))
# # r2 = np.random.randn(len(t))
# # npm = np.matrix([t, r1, r2])

# r1 = np.random.randn(len(t))
# npm = np.matrix([t])

# data.append(npm)

# t += 1
# # npm = np.matrix([t, r1, r2])
# # data.append(npm)
# npm = np.matrix([t])

# data.append(npm)

# dmat = np.concatenate(data, axis=1)

# print dmat[:,]

# npa = np.array(range(0, 10))
# print dmat
# gu = graphs.GraphUpdater()
# gu.add_data(npa, ["npa"])

# print gu.data["npa"]

# graph = graphs.Graph(legend=False)

# app.add_widget(graph)
# app.run()
