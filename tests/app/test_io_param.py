#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-30 01:47:19

import sys
sys.path.append('/home/cosgroma/workspace/libs/python/modules')

from QtBooty import App
from QtBooty import framework

app = App()

io_grid = framework.IOGrid()

groups = [dict()]
groups[-1]["name"] = "class::label"
groups[-1]["box_enabled"] = False
groups[-1]["box_name"] = "class::label"
groups[-1]["layout"] = ["h", "na"]

# label_defaults = {"label": ""}
groups[-1]["items"] = [
  {
    "name": "regular",
    "class": "label",
    "config": {
      "name": "regular",
      "label": "regular label"
    }
  }
]

groups.append(dict())
groups[-1]["name"] = "class::edit"
groups[-1]["box_enabled"] = True
groups[-1]["box_name"] = "class::edit"
groups[-1]["layout"] = ["h", "na"]

groups[-1]["items"] = [
  {
    "name": "edit0",
    "class": "edit",
    "config": {
      "name": "edit0",
      "label": "normal",
      "position": "above"
    }
  }, {
    "name": "edit2",
    "class": "edit",
    "config": {
      "name": "edit2",
      "type": "spin",
      "position": "above",
      "label": "spin"
    }
  }
]

groups.append(dict())
groups[-1]["name"] = "class::button"
groups[-1]["box_enabled"] = True
groups[-1]["box_name"] = "class::button"
groups[-1]["layout"] = ["h", "na"]

groups[-1]["items"] = [
  {
    "name": "button1",
    "class": "button",
    "config": {
      "name": "button1",
      "label": "button1",
      "args": ["normal"]
    }
  }, {
    "name": "button2",
    "class": "button",
    "config": {
      "name": "button2",
      "type": "radio",
      "label": "radio button",
      "args": ["radio"]
    }
  }

]


groups.append(dict())
groups[-1]["name"] = "scrollable::slider"
groups[-1]["box_enabled"] = True
groups[-1]["box_name"] = "scrollable::slider"
groups[-1]["scrollable"] = True
groups[-1]["layout"] = ["h", "c"]

def slider_callback(args):
  print "got callback"

groups[-1]["items"] = []
for i in range(0, 10):
  groups[-1]["items"].append(
    {
      "name": "slider%d" % i,
      "class": "slider",
      "config": {
        "name": "slider%d" % i,
        "label": "slider%d" % i,
        "display": True,
        "orientation": "v",
        "args": ["dB"]
      }
    }
  )


## If anything changes in the tree, print a message
def change(param, changes):
    print("tree changes:")
    for param, change, data in changes:
        path = p.childPath(param)
        if path is not None:
            childName = '.'.join(path)
        else:
            childName = param.name()
        print('  parameter: %s'% childName)
        print('  change:    %s'% change)
        print('  data:      %s'% str(data))
        print('  ----------')



config = io_grid.config_init(len(groups), [len(g["items"]) for g in groups])

config["layout"] = ["v", "t"]
[d.update(u) for d, u in zip(config["groups"], groups)]
# config["groups"].update(groups)

p = io_grid.config_widget(config)
p.sigTreeStateChanged.connect(change)
app.add_widget(io_grid)
app.run()


# def changeStyle(self, styleName):
#         QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(styleName))
#         self.changePalette()

#     def changePalette(self):
#         if (self.useStylePaletteCheckBox.isChecked()):
#             QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())
#         else:
#             QtGui.QApplication.setPalette(self.originalPalette)


