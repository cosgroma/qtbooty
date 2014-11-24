#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2014-11-26 08:14:44

import sys
sys.path.append('/Users/cosgroma/workspace/sergeant/guis')

import psutil
import time

from QtBooty import App
from QtBooty import graphs
from QtBooty import framework

def test_trigger():
  print("yo")

app = App('app_config.json')
app.main.menus["View"].actions["CPU Statistics"].triggered.connect()

tabs = framework.Tabs()
app.add_widget(tabs)

ts_static = graphs.TimeSeries()
tabs.add_tab(ts_static, 'ts_static')
ts_static.run_test()
# ts_static.start()

ts_dynamic = graphs.TimeSeries(interval=50, maxlen=1000)
tabs.add_tab(ts_dynamic, 'ts_dynamic')
ts_dynamic.run_test(interval=50, dynamic=True, freqs=[.1, .2, .3])





app.add_timer(500, psutil_data_update)
cpu_usage.start()
app.run()


