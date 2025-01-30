import unittest
from src.FUV import FUV as function

rows, cols = 15, 15  
class TestFUV(unittest.TestCase):
    """Test suite for Final Unlocking Vector.

    Condition: For FUV[i] to be true, either PUV[i] is False or for all j, PUM[i][j] must be true.
    """
    
    def test_PUV_all_false(self):
        """Test when every element of PUV is False, that all elements of FUV are True"""
        PUM = [[False] * cols for _ in range(rows)]
        PUV = [False for _ in range(rows)]
        FUV = function(PUM, PUV)
        for i in range(rows):
            self.assertTrue(FUV[i])
    def test_PUV_and_PUM_all_true(self):
        """Test when all the PUM is True and the PUV is all True (to make the PUM matter), that we get a completly True FUV"""
        PUM = [[True] * cols for _ in range(rows)]
        PUV = [True for _ in range(rows)]
        FUV = function(PUM, PUV)
        for i in range(rows):
            self.assertTrue(FUV[i])
    
    def test_PUM_all_false(self):
        """Test when all the PUM is False and the PUV is all True (to make the PUM matter), that all elements of FUV are False"""
        PUM = [[False] * cols for _ in range(rows)]
        PUV = [True for _ in range(rows)]
        FUV = function(PUM, PUV)
        for i in range(rows):
            self.assertFalse(FUV[i])
    def test_PUM_one_false_in_every_row(self):
        """Test when exactly one element per row of PUM is False and all the PUV is True (to make the PUM matter),
        that all the FUV is False"""
        PUM = [[True] * cols for _ in range(rows)]
        PUV = [True for _ in range(rows)]
        for i in range(rows):
            PUM[i][i] = False
        FUV = function(PUM, PUV)
        for i in range(rows):
            self.assertFalse(FUV[i])

    def test_general_PUM_and_PUV(self):
        """Test a general non specific example"""
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