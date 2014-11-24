#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-26 08:07:43
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2014-11-26 08:09:56

from QtBooty import graphs

class CpuStats():

  cpu_usage = graphs.TimeSeries(interval=1000, ylim=[0,100])
  app.add_widget(cpu_usage)

  psutil.cpu_percent(interval=None)
  start_time = time.time()

  for p in range(0, psutil.cpu_count()):
    cpu_usage.add_line(p, color='r')

  def psutil_data_update():
    usage = psutil.cpu_percent(interval=None, percpu=True)
    t = time.time() - start_time
    for p in range(0, psutil.cpu_count()):
      cpu_usage.add_data_point(p, t, usage[p])
