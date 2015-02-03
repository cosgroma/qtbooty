#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-02-03 06:40:01

import sys
sys.path.append('/Users/cosgroma/workspace')

# import psutil
import time

from QtBooty import App
from QtBooty import graphs
from QtBooty import framework


from pyqtgraph.flowchart import Flowchart
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import pyqtgraph.metaarray as metaarray

def test_trigger():
  print("yo")

app = App('../config/app_config.json')
# app.main.menus["View"].actions["CPU Statistics"].triggered.connect()

tabs = framework.Tabs()


# ## Create flowchart, define input/output terminals
# fc = Flowchart(terminals={
#     'dataIn': {'io': 'in'},
#     'dataOut': {'io': 'out'}
# })

# print dir(fc)
# # print type(fc)
# w = fc.widget()

# for c in fc.widget().children():
#   print type(c)
#   for c1 in c.children():
#     print type(c1)
#     for c2 in c1.children():
#       print type(c2)
#       for c3 in c2.children():
#         print type(c3)
## Add flowchart control panel to the main window
# layout.addWidget(fc.widget(), 0, 0, 2, 1)

# app.add_widget(w)

# app.add_timer(500, psutil_data_update)
# cpu_usage.start()
app.run()








# ## Add two plot widgets
# pw1 = pg.PlotWidget()
# pw2 = pg.PlotWidget()
# layout.addWidget(pw1, 0, 1)
# layout.addWidget(pw2, 1, 1)



# ## generate signal data to pass through the flowchart
# data = np.random.normal(size=1000)
# data[200:300] += 1
# data += np.sin(np.linspace(0, 100, 1000))
# data = metaarray.MetaArray(data, info=[{'name': 'Time', 'values': np.linspace(0, 1.0, len(data))}, {}])

# ## Feed data into the input terminal of the flowchart
# fc.setInput(dataIn=data)

# ## populate the flowchart with a basic set of processing nodes.
# ## (usually we let the user do this)
# plotList = {'Top Plot': pw1, 'Bottom Plot': pw2}

# pw1Node = fc.createNode('PlotWidget', pos=(0, -150))
# pw1Node.setPlotList(plotList)
# pw1Node.setPlot(pw1)

# pw2Node = fc.createNode('PlotWidget', pos=(150, -150))
# pw2Node.setPlot(pw2)
# pw2Node.setPlotList(plotList)

# fNode = fc.createNode('GaussianFilter', pos=(0, 0))
# fNode.ctrls['sigma'].setValue(5)
# fc.connectTerminals(fc['dataIn'], fNode['In'])
# fc.connectTerminals(fc['dataIn'], pw1Node['In'])
# fc.connectTerminals(fNode['Out'], pw2Node['In'])
# fc.connectTerminals(fNode['Out'], fc['dataOut'])






