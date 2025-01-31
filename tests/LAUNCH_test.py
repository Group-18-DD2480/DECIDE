import unittest

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from LAUNCH import LAUNCH
from utils import InvalidInputException

class Test_LAUNCH(unittest.TestCase):

    def test_LAUNCH_positive(self):
        # FUV is a correct sized vector and all entries are True
        FUV = [True for _ in range(15)]
        self.assertTrue(LAUNCH(FUV))

    def test_LAUNCH_negative(self):
        # FUV is a correct sized vector but at least one entry is False
        FUV = [False for _ in range(15)]
        self.assertFalse(LAUNCH(FUV))

    def test_LAUNCH_invalid(self):
        # size of FUV is not correct
        FUV = [True, True]
        self.assertRaises(InvalidInputException, LAUNCH, FUV)