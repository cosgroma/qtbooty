#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-02-03 21:41:08

import sys
sys.path.append('/home/cosgroma/workspace/libs/python/modules')

from QtBooty import App
from QtBooty import framework

config = dict()

app = App()

io_grid = framework.IOGrid()

groups = [dict()]
groups[-1]["name"] = "class::label"
groups[-1]["enabled"] = True
groups[-1]["box_enabled"] = False
groups[-1]["group_name"] = "class::label"
groups[-1]["layout"] = ["h", "na"]

# label_defaults = {"label": ""}
groups[-1]["items"] = [
  {
    "class": "label",
    "label": "regular label",
    "name": "genlab"
  }
]

groups.append(dict())
groups[-1]["name"] = "class::edit"
groups[-1]["enabled"] = True
groups[-1]["box_enabled"] = True
groups[-1]["group_name"] = "class::edit"
groups[-1]["layout"] = ["h", "na"]

# edit_defaults = {
#   "qtype":            "default",
#   "label":           None,
#   "position":        "left",
#   "default":         None,
#   "editingFinished": None,
#   "args":            None
# }

def test_edit_finish(args):
  print args[0].text()


groups[-1]["items"] = [
  {
    "class": "edit",
    "name": "normali",
      "label": "normal::intv",
      "dtype": "int",
      "position": "above",
      "editingFinished": test_edit_finish,
      "args": ["test"],
      "tool-tip": "test tip"
  },{
    "class": "edit",
    "name": "normalf",
      "label": "normal::floatv",
      "dtype": "float",
      "position": "above",
      "editingFinished": test_edit_finish,
      "args": ["test"]
  }, {
    "class": "edit",
    "name": "datetime",
      "qtype": "datetime",
      "position": "above",
      "label": "date time"
  }, {
    "class": "edit",
    "name": "spin",
      "qtype": "spin",
      "position": "above",
      "label": "spin"
  }
]

groups.append(dict())
groups[-1]["name"] = "class::button"
groups[-1]["enabled"] = True
groups[-1]["box_enabled"] = True
groups[-1]["group_name"] = "class::button"
groups[-1]["layout"] = ["h", "na"]

def test_clicked(button):
  print("Button pressed: %s" % button.text())

# button_defaults = {
#   "qtype":    "default",
#   "label":   "",
#   "clicked": None,
#   "args":    None

groups[-1]["items"] = [
  {
    "class": "button",
    "name": "button1",
      "label": "button1",
      "clicked": test_clicked,
      "args": ["normal"]
  }, {
    "class": "button",
    "name": "radio",
      "qtype": "radio",
      "label": "radio button",
      "clicked": test_clicked,
      "args": ["radio"]
  }

]

# slider_defaults = {
#   "qtype":         "default",
#   "label":        "",
#   "position":     "above",
#   "range":        [0, 100],
#   "orientation":  "v",
#   "policy":       "expand",
#   "display":      False,
#   "valueChanged": None,
#   "args":         [None]

groups.append(dict())

groups[-1]["enabled"] = True
groups[-1]["box_enabled"] = True
groups[-1]["group_name"] = "scrollable::slider"
groups[-1]["scrollable"] = True
groups[-1]["layout"] = ["h", "c"]

def slider_callback(args):
  print "got callback"

groups[-1]["items"] = []
for i in range(0, 10):
  groups[-1]["items"].append(
    {
      "class": "slider",
      "name": "slider%d" % i,
        "label": "slider%d" % i,
        "display": True,
        "orientation": "v",
        # "policy": "smart",
        "valueChanged": slider_callback,
        "args": ["dB"]
    }
  )

groups.append(dict())
groups[-1]["enabled"] = True
groups[-1]["box_enabled"] = True
groups[-1]["group_name"] = "slider::scroll"
groups[-1]["layout"] = ["h", "na"]

groups[-1]["items"] = [
 {
  "class": "slider",
    "name": "scroll",
      "qtype": "scroll",
      "label": "slider::scroll",
      "display": True,
      "orientation": "v",
      "valueChanged": slider_callback,
      "args": [""]
  }
]

groups.append(dict())
groups[-1]["enabled"] = True
groups[-1]["box_enabled"] = True
groups[-1]["group_name"] = "slider::dials"
groups[-1]["layout"] = ["h", "l"]

groups[-1]["items"] = [
 {
  "class": "slider",
    "name": "dial",
      "qtype": "dial",
      "label": "dial0",
      "display": True,
      "orientation": "v",
      "valueChanged": slider_callback,
      "args": [u"°"]
  }, {
  "class": "slider",
    "name": "dial1",
      "qtype": "dial",
      "label": "dial1",
      "display": True,
      "orientation": "v",
      "valueChanged": slider_callback,
      "args": [u"°"]
  }
]

groups.append(dict())
groups[-1]["enabled"] = True
groups[-1]["box_enabled"] = True
groups[-1]["group_name"] = "combobox::default"
groups[-1]["layout"] = ["h", "c"]

# combo_defaults = {
#   "label":           "combobox",
#   "items":           [],
#   "maxVisible":      10,
#   "default":         None,
#   "activated":       None,
#   "indexChanged":    None,
#   "args":            None

groups[-1]["items"] = [
 {
  "class": "combo",
    "name": "combobox",
      "label":           "combobox",
      "items":           ["one", "two", "three"],
      "maxVisible":      10,
      "activated":       None,
      "indexChanged":    None,
      "args":            None
  }
]


groups.append(dict())
groups[-1]["enabled"] = True
groups[-1]["box_enabled"] = True
groups[-1]["group_name"] = "table::default"
groups[-1]["layout"] = ["h", "c"]

# table_defaults = {
#   "label": "table",
#   "headers": [],
#   "items": [],
#   "args": None
# }

groups[-1]["items"] = [
 {
  "class": "table",
    "name": "table",
      "label":   "table",
      "headers": ["one", "two"],
      "items":   [[1, 2], [3,4], [5,6]],
      "args":    None
  }
]

# for g in groups:
#   print g["enabled"], g["group_name"]

# print len(groups)
config = io_grid.config_init(len(groups), [len(g["items"]) for g in groups])
# config= dict()
# config["groups"] = groups
config["layout"] = ["v", "b"]
[d.update(u) for d, u in zip(config["groups"], groups)]
# print config
# # config["groups"].update(groups)

io_grid.config_widget(config)
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


