#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Mathew Cosgrove
# @Date:   2014-11-22 23:14:38
# @Last Modified by:   cosgrma
# @Last Modified time: 2015-09-04 01:44:22


import logging
import pyutils
pyutils.setup_logging()
logger = logging.getLogger()
from QtBooty import App
import os


def test_trigger():
  print("test")
  os.startfile("C:\cygwin\home\cosgrma\workspace\sergeant\guis\pash\src\pash\gperfmon.py")


if __name__ == '__main__':
  app = App('config/bad_app_config.json')
  app.main.menus["File"].actions["New"].triggered.connect(test_trigger)
  app.run()
