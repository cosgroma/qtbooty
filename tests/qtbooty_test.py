#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-22 23:14:38
# @Last Modified by:   Mathew Cosgrove
# @Last Modified time: 2016-04-13 03:36:01


import logging
import pyutils
pyutils.setup_logging()
logger = logging.getLogger()
from QtBooty import App
import os


def test_trigger():
  print("test")
  # os.startfile("")


if __name__ == '__main__':
  app = App('config/bad_app_config.json')
  # app.main.menus["File"].actions["New"].triggered.connect(test_trigger)
  app.run()
