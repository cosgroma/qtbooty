#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-22 23:14:38
# @Last Modified by:   cosgroma
# @Last Modified time: 2014-11-23 02:40:27

from QtBooty import App

def test_trigger():
  print("test")

if __name__ == '__main__':
  app = App.App('app_config.json')
  app.main_window.menus["File"].actions["New"].triggered.connect(test_trigger)
  app.run()
