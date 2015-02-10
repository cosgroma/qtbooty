#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   cosgroma
# @Last Modified time: 2015-01-20 12:48:58

import sys
# sys.path.append('/home/cosgroma/workspace/sergeant/guis')

from QtBooty import App
from QtBooty import graphs
from collections import deque
import numpy as np



app = App('../config/app_config.json')

time_series = graphs.PointSeries()

line_sine = "sin"
line_cosine = "cos"
time_series.add_line(line_sine, color='r')
time_series.add_line(line_cosine, color='b')
time_series.add_controller()


f = .3

interval_sine = 10
ts = 0.0
def update_sine():
  global ts
  ts += (interval_sine/1000.0)
  ys = np.sin(2*np.pi*f*ts)
  time_series.add_data_point(line_sine, ts, ys)

interval_cosine = 10
tc = 0.0
cosine_removed = False

def update_cosine():
  global tc
  global cosine_removed
  tc += (interval_cosine/1000.0)
  # if tc > 6 and tc < 8 and not cosine_removed:
  #   time_series.remove_line(line_cosine)
  #   cosine_removed = True
  # elif tc > 8 and cosine_removed:
  #   print("would add cosine back in")
  #   time_series.add_line(line_cosine, color='b')
  #   cosine_removed = False
  # elif not cosine_removed:
  yc = np.cos(2*np.pi*f*tc)
  time_series.add_data_point(line_cosine, tc, yc)


app.add_widget(time_series)

app.add_timer(interval_sine, update_sine)
app.add_timer(interval_cosine, update_cosine)
time_series.set_interval(50)
time_series.start()

app.run()
