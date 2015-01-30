#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-25 21:43:42
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2015-01-29 16:38:10

import sys
sys.path.append('/Users/cosgroma/workspace')

from QtBooty import App
from QtBooty import framework

app = App()

io_grid = framework.IOGrid()

groups = [dict()]

groups[-1]["box_enabled"] = False
groups[-1]["box_name"] = "class::label"
groups[-1]["layout"] = ["h", "na"]

# label_defaults = {"label": ""}
groups[-1]["items"] = [
  {
    "class": "label",
    "config": {
      "label": "regular label"
    }
  }
]

groups.append(dict())
groups[-1]["box_enabled"] = True
groups[-1]["box_name"] = "class::edit"
groups[-1]["layout"] = ["h", "na"]

# edit_defaults = {
#   "type":            "default",
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
    "config": {
      "label": "normal",
      "position": "above",
      "editingFinished": test_edit_finish,
      "args": ["test"]
    }
  }, {
    "class": "edit",
    "config": {
      "type": "datetime",
      "position": "above",
      "label": "date time"
    }
  }, {
    "class": "edit",
    "config": {
      "type": "spin",
      "position": "above",
      "label": "spin"
    }
  }
]


groups.append(dict())
groups[-1]["box_enabled"] = True
groups[-1]["box_name"] = "class::button"
groups[-1]["layout"] = ["h", "na"]

def test_clicked(button):
  print("Button pressed: %s" % button.text())

# button_defaults = {
#   "type":    "default",
#   "label":   "",
#   "clicked": None,
#   "args":    None
# }

groups[-1]["items"] = [
  {
    "class": "button",
    "config": {
      "label": "button1",
      "clicked": test_clicked,
      "args": ["normal"]
    }
  }, {
    "class": "button",
    "config": {
      "type": "radio",
      "label": "radio button",
      "clicked": test_clicked,
      "args": ["radio"]
    }
  }

]

# slider_defaults = {
#   "type":         "default",
#   "label":        "",
#   "position":     "above",
#   "range":        [0, 100],
#   "orientation":  "h",
#   "policy":       "expand",
#   "display":      False,
#   "valueChanged": None,
#   "args":         [None]
# }

groups.append(dict())
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
      "class": "slider",
      "config": {
        "label": "slider%d" % i,
        "display": True,
        "orientation": "v",
        # "policy": "smart",
        "valueChanged": slider_callback,
        "args": ["dB"]
      }
    }
  )

groups.append(dict())
groups[-1]["box_enabled"] = True
groups[-1]["box_name"] = "slider::scroll"
groups[-1]["layout"] = ["h", "na"]

groups[-1]["items"] = [
 {
  "class": "slider",
    "config": {
      "type": "scroll",
      "label": "slider::scroll",
      "display": True,
      "orientation": "h",
      "valueChanged": slider_callback,
      "args": [""]
    }
  }
]

groups.append(dict())
groups[-1]["box_enabled"] = True
groups[-1]["box_name"] = "slider::dials"
groups[-1]["layout"] = ["h", "l"]

groups[-1]["items"] = [
 {
  "class": "slider",
    "config": {
      "type": "dial",
      "label": "dial0",
      "display": True,
      "orientation": "v",
      "valueChanged": slider_callback,
      "args": [u"°"]
    }
  }, {
  "class": "slider",
    "config": {
      "type": "dial",
      "label": "dial1",
      "display": True,
      "orientation": "v",
      "valueChanged": slider_callback,
      "args": [u"°"]
    }
  }
]

groups.append(dict())
groups[-1]["box_enabled"] = True
groups[-1]["box_name"] = "combobox::default"
groups[-1]["layout"] = ["h", "c"]

# combo_defaults = {
#   "label":           "combobox",
#   "items":           [],
#   "maxVisible":      10,
#   "default":         None,
#   "activated":       None,
#   "indexChanged":    None,
#   "args":            None
# }

groups[-1]["items"] = [
 {
  "class": "combo",
    "config": {
      "label":           "combobox",
      "items":           ["one", "two", "three"],
      "maxVisible":      10,
      "activated":       None,
      "indexChanged":    None,
      "args":            None
    }
  }
]


groups.append(dict())
groups[-1]["box_enabled"] = True
groups[-1]["box_name"] = "table::default"
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
    "config": {
      "label":   "table",
      "headers": ["one", "two"],
      "items":   [[1, 2], [3,4], [5,6]],
      "args":    None
    }
  }
]
config = io_grid.config_init(len(groups), [len(g["items"]) for g in groups])

config["layout"] = ["v", "t"]
[d.update(u) for d, u in zip(config["groups"], groups)]
# config["groups"].update(groups)

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


