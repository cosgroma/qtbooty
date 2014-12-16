#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-22 23:14:38
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2014-12-05 21:26:57

from QtBooty import App

def test_trigger():
  print("test")

if __name__ == '__main__':
  app = App('config/app_config.json')
  app.main.menus["File"].actions["New"].triggered.connect(test_trigger)
  app.run()
