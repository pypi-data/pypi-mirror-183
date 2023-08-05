import unittest

import logging
logger = logging.getLogger(__name__)

from . import *


class TemplateTest(unittest.TestCase):
    def test_root(self):
        success = True
        self.assertEqual(success, True)
