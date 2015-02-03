#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-26 08:07:43
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-02-03 09:35:45
import sys
sys.path.append('/home/cosgroma/workspace/lib/python/modules')
from PyQt4 import QtCore, QtGui
from QtBooty import App
from QtBooty import graphs
import psutil
import numpy as np

class CpuThread(QtCore.QThread):
  cpustats = QtCore.pyqtSignal(list)
  diskstats = QtCore.pyqtSignal(list)
  def __init__(self, parent=None):
    super(CpuThread, self).__init__(parent)
    self.start(QtCore.QThread.LowPriority)
    self.count = 0.0
  def run(self):
    while True:
      self.usleep(1000)
      usage = psutil.cpu_percent(interval=1, percpu=True)
      self.cpustats.emit(usage)

      self.usleep(10000)
      disk = psutil.disk_io_counters()
      self.diskstats.emit([disk.read_count, disk.write_count])

class CpuStatsPlot(object):
  """docstring for CpuStatsPlot"""
  def __init__(self, ts_updater, disk_updater):
    super(CpuStatsPlot, self).__init__()
    self.cputhread = CpuThread()
    self.ts_updater = ts_updater
    self.plotconfig = dict()
    self.diskplotconfig = dict()
    self.cputhread.cpustats.connect(self.updatePlot)
    self.cputhread.diskstats.connect(self.updateDisk)
    self.count = 0.0
    self.configured = False
    self.diskplotconfig["plots"] = [
      {"name":"readcount", "plot kwargs": {"pen": "r"}},
      {"name":"write_count", "plot kwargs": {"pen": "b"}}]
    self.disk_updater = disk_updater
  def updateDisk(self, diskio):
    npm = np.matrix([
      [self.count],
      [diskio[0]],
      [diskio[1]]
      ])
    self.disk_updater.add_data(npm, self.diskplotconfig)
  def updatePlot(self, usage):
    if not self.configured:
      self.plotconfig["plots"] = []
      for i in range(0, len(usage)):
        self.plotconfig["plots"].append({
          "name": "cpu%d" % i,
          "plot kwargs": {
            "pen": QtGui.QPen(
              QtGui.QColor(
                np.random.randint(255),
                np.random.randint(255),
                np.random.randint(255)
              )
            ), "downsample": None
          }
        })
      self.configured = True
    npm = np.zeros((len(usage) + 1, 1))

    self.count += 1.0
    npm[:, 0] = self.count
    npm[1:, 0] = usage
    self.ts_updater.add_data(npm, self.plotconfig)



app = App('../tests/config/app_config.json')

timeseries = graphs.Line(legend=True, controller=True)
diskts = graphs.Line(legend=True, controller=True)

gscheduler = graphs.GraphScheduler()
ts_updater = gscheduler.add_graph(timeseries, maxlen=1000, interval=1000)
ds_updater = gscheduler.add_graph(diskts, maxlen=1000, interval=1000)

plot = CpuStatsPlot(ts_updater, ds_updater)

app.add_widget(timeseries)
app.add_widget(diskts)
gscheduler.start()
app.run()


# time.sleep(10)


# thread.join()
# 'AccessDenied'
# 'BOOT_TIME'
# 'CONN_CLOSE'
# 'CONN_CLOSE_WAIT'
# 'CONN_CLOSING'
# 'CONN_ESTABLISHED'
# 'CONN_FIN_WAIT1'
# 'CONN_FIN_WAIT2'
# 'CONN_LAST_ACK'
# 'CONN_LISTEN'
# 'CONN_NONE'
# 'CONN_SYN_RECV'
# 'CONN_SYN_SENT'
# 'CONN_TIME_WAIT'
# 'Error'
# 'NUM_CPUS'
# 'NoSuchProcess'
# 'Popen'
# 'Process'
# 'STATUS_DEAD'
# 'STATUS_DISK_SLEEP'
# 'STATUS_IDLE'
# 'STATUS_LOCKED'
# 'STATUS_RUNNING'
# 'STATUS_SLEEPING'
# 'STATUS_STOPPED'
# 'STATUS_TRACING_STOP'
# 'STATUS_WAITING'
# 'STATUS_WAKING'
# 'STATUS_ZOMBIE'
# 'TOTAL_PHYMEM'
# 'TimeoutExpired'
# '_POSIX'
# '_PY3'
# '_TOTAL_PHYMEM'
# '_WINDOWS'
# '__all__'
# '__author__'
# '__builtins__'
# '__class__'
# '__delattr__'
# '__dict__'
# '__doc__'
# '__file__'
# '__format__'
# '__getattribute__'
# '__hash__'
# '__init__'
# '__module__'
# '__name__'
# '__new__'
# '__package__'
# '__path__'
# '__reduce__'
# '__reduce_ex__'
# '__repr__'
# '__setattr__'
# '__sizeof__'
# '__str__'
# '__subclasshook__'
# '__version__'
# '__weakref__'
# '_assert_pid_not_reused'
# '_common'
# '_compat'
# '_deprecated'
# '_deprecated_method'
# '_last_cpu_times'
# '_last_cpu_times_2'
# '_last_per_cpu_times'
# '_last_per_cpu_times_2'
# '_module'
# '_nt_sys_diskio'
# '_nt_sys_netio'
# '_pmap'
# '_psosx'
# '_psplatform'
# '_psposix'
# '_timer'
# '_wraps'
# 'avail_phymem'
# 'avail_virtmem'
# 'boot_time'
# 'callable'
# 'cpu_count'
# 'cpu_percent'
# 'cpu_times'
# 'cpu_times_percent'
# 'defaultdict'
# 'disk_io_counters'
# 'disk_partitions'
# 'disk_usage'
# 'errno'
# 'get_pid_list'
# 'get_process_list'
# 'get_users'
# 'long'
# 'net_connections'
# 'net_io_counters'
# 'network_io_counters'
# 'os'
# 'phymem_usage'
# 'pid_exists'
# 'pids'
# 'process_iter'
# 'pwd'
# 'signal'
# 'subprocess'
# 'swap_memory'
# 'sys'
# 'test'
# 'time'
# 'total_virtmem'
# 'used_phymem'
# 'used_virtmem'
# 'users'
# 'version_info'
# 'virtmem_usage'
# 'virtual_memory'
# 'wait_procs'
# 'warnings'
