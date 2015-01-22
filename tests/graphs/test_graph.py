#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-21 13:45:19

import sys
# sys.path.append('/home/cosgroma/workspace/sergeant/guis')

from QtBooty import App
from QtBooty import graphs
from collections import deque
import numpy as np

# app = App('../config/app_config.json')
t = np.linspace(0, 1, 8, endpoint=False)
# t = np.array([1])
r1 = np.random.randn(len(t))
r2 = np.random.randn(len(t))
npm = np.matrix([t, r1, r2])
data = deque(maxlen=10)
data.append(npm)
t += 1
npm = np.matrix([t, r1, r2])
data.append(npm)
dmat = np.concatenate(data, axis=1)
print dmat.shape
print dmat[:,]

npa = np.array(range(0,10))
# print dmat

print npa.shape

# gu = graphs.GraphUpdater()
# gu.add_data(npa, ["npa"])

# print gu.data["npa"]

# graph = graphs.Graph(legend=False)

# app.add_widget(graph)
# app.run()
