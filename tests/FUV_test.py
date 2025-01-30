import unittest
from src.FUV import FUV as function

rows, cols = 15, 15  
class TestFUV(unittest.TestCase):
    
    def test_PUV_all_false(self):
        PUM = [[False] * cols for _ in range(rows)]
        PUV = [False for _ in range(rows)]
        FUV = function(PUM, PUV)
        for i in range(rows):
            self.assertTrue(FUV[i])
    def test_PUV_and_PUM_all_true(self):
        PUM = [[True] * cols for _ in range(rows)]
        PUV = [True for _ in range(rows)]
        FUV = function(PUM, PUV)
        for i in range(rows):
            self.assertTrue(FUV[i])
    
    def test_PUM_all_false(self):
        PUM = [[False] * cols for _ in range(rows)]
        PUV = [True for _ in range(rows)]
        FUV = function(PUM, PUV)
        for i in range(rows):
            self.assertFalse(FUV[i])
    def test_PUM_one_false_in_every_row(self):
        PUM = [[True] * cols for _ in range(rows)]
        PUV = [True for _ in range(rows)]
        for i in range(rows):
            PUM[i][i] = False
        FUV = function(PUM, PUV)
        for i in range(rows):
            self.assertFalse(FUV[i])
    def test_general_PUM_and_PUV(self):
        PUM = [
            [False, True, True, True, True, True, True, True, False, False, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, False, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, False, False, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, False, True, False, True, True, True, False],
            [True, True, True, True, False, True, True, True, False, False, False, True, True, True, True],
            
            [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, False, True, True, True, True, True, True, False, False, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, False, False, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, False, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, False, True, False, True, True, True, True],
            
            [True, True, True, True, True, True, True, True, False, False, False, True, True, True, True],
            [True, True, True, True, True, False, True, True, False, False, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, False, False, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
        ]
        PUV = [False, True, False, True, True, 
               True, True, True, False, False, 
               True, True, False, True, True]
        FUV_func = function(PUM,PUV)
        FUV_test = [True, False, True, False, False, 
                    True, False, False, True, True,
                    False, False, True, True, True]
        self.assertEqual(FUV_func, FUV_test)