#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2016-06-16 23:52:21

import logging
try:
  import pyutils
  pyutils.setup_logging()
except:
  pass

logger = logging.getLogger()

import os
os.environ['QT_API'] = 'pyqt'

import numpy as np

import sys
sys.path.append(os.path.dirname(os.path.join(os.path.dirname(__file__), "../../qtbooty")))

from qtbooty import App
from qtbooty import graph

controller_config = {
    "layout": ["h", "na"],
    "groups": [
        {
            "enabled": True,
            "box_enabled": True,
            "group_name": "signal::controller",
            "layout": [
                "v",
                "t"
            ],
            "items": [
                {
                    "class": "slider",
                    "name": "power0",
                    "label": "Power",
                    "display": True,
                    "orientation": "v",
                    "policy": "smart",
                    "args": [
                        "dB"
                    ]
                },
                {
                    "class": "slider",
                    "name": "doppler1",
                    "qtype": "dial",
                    "label": "Doppler",
                    "display": True,
                    "orientation": "v",
                    "range": [-5000.0,
                              5000.0
                              ],
                    "policy": "smart",
                    "args": [
                        "Hz"
                    ]
                }]
        }]}

app = App('../config/app_config.json')
time_series = graph.Line(legend=True, controller=False)

gscheduler = graph.GraphScheduler()
ts_updater = gscheduler.add_graph(time_series, maxlen=1000, interval=50)


def update():
  npm = np.matrix([
      update.t,
      10 * np.cos(2 * np.pi * .3 * update.t),
      10 * np.sin(2 * np.pi * .6 * update.t)
  ])
  ts_updater.add_data(npm, update.config)
  update.t += update.intr / 1000.0

update.intr = 10.0
# update.t = np.array([0.0])
update.t = np.linspace(0, update.intr / 1000.0, 10, endpoint=False)

update.config = {
    "plots": [{
        "name": "I",
        "plot kwargs": {
            "pen": 'r',
            "downsample": None,
            "fillLevel": 0,
            "brush": (0, 0, 255, 80)
        }
    }, {
        "name": "Q",
        "plot kwargs": {
            "pen": 'r',
            "downsample": None,
            "fillLevel": 0,
            "brush": (0, 0, 255, 80)
        }
    }]
}


app.add_widget(time_series)
app.add_timer(update.intr, update)
gscheduler.start()
app.run()
