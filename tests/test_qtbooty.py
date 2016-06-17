#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_qtbooty
----------------------------------

Tests for `qtbooty` module.
"""

# import unittest

# from qtbooty import qtbooty


# class Testqtbooty(unittest.TestCase):

#     def setUp(self):
#         pass

#     def tearDown(self):
#         pass

#     def test_000_something(self):
#         pass


# if __name__ == '__main__':
#     import sys
#     sys.exit(unittest.main())


import sys
import os

import logging
try:
  import pyutils
  pyutils.setup_logging()
except:
  pass
logger = logging.getLogger()

sys.path.append(os.path.dirname(os.path.join(os.path.dirname(__file__), "../qtbooty")))

from qtbooty import App
import os


def test_trigger():
  print("test")
  # os.startfile("")

if __name__ == '__main__':
  app = App('config/app_config.json')
  # app.main.menus["File"].actions["New"].triggered.connect(test_trigger)
  app.run()
