import unittest
from src.FUV import FUV as function
from src.utils import InvalidInputException


rows, cols = 15, 15  
class TestFUV(unittest.TestCase):
    """Test suite for Final Unlocking Vector.

    Condition: For FUV[i] to be true, either PUV[i] is False or for all j, PUM[i][j] must be true except for PUM[i][i].
    """
    def test_invalid_PUV_not_list(self):
        """Test that FUV fails when PUM isn't a list"""
        PUM = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            PUM[i][i] = None
        PUV = 3
        self.assertRaises(InvalidInputException,function,PUM,PUV)
    def test_invalid_PUM_not_list(self):
        """Test that FUV fails when PUV isn't a list"""
        PUM = 1
        PUV = [True for _ in range(rows)]
        self.assertRaises(InvalidInputException,function,PUM,PUV)
    def test_invalid_input_sizes(self):
        """Test that FUV fails when PUM and PUM's sizes don't match"""
        PUM = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            PUM[i][i] = None
        PUV = [True for _ in range(rows+1)]
        self.assertRaises(InvalidInputException,function,PUM,PUV)
    def test_invalid_PUM_symetric(self):
        """Test that FUV fails when PUM isn't a symetric"""
        PUM = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            PUM[i][i] = None
        PUV = [True for _ in range(rows)]
        PUM[0][1] = True
        self.assertRaises(InvalidInputException,function,PUM,PUV)
    def test_invalid_PUM_None(self):
        """Test that FUV fails when PUM doesn't have None on the diagonal"""
        PUM = [[False] * cols for _ in range(rows)]
        PUV = [True for _ in range(rows)]
        self.assertRaises(InvalidInputException,function,PUM,PUV)


    def test_PUV_all_false(self):
        """Test when every element of PUV is False, that all elements of FUV are True"""
        PUM = [[False] * cols for _ in range(rows)]
        PUV = [False for _ in range(rows)]
        for i in range(rows):
            PUM[i][i] = None
        FUV = function(PUM, PUV)
        for i in range(rows):
            self.assertTrue(FUV[i])
    def test_PUV_and_PUM_all_true(self):
        """Test when all the PUM is True and the PUV is all True (to make the PUM matter), that we get a completly True FUV"""
        PUM = [[True] * cols for _ in range(rows)]
        PUV = [True for _ in range(rows)]
        for i in range(rows):
            PUM[i][i] = None
        FUV = function(PUM, PUV)
        for i in range(rows):
            self.assertTrue(FUV[i])
    
    def test_PUM_all_false(self):
        """Test when all the PUM is False and the PUV is all True (to make the PUM matter), that all elements of FUV are False"""
        PUM = [[False] * cols for _ in range(rows)]
        PUV = [True for _ in range(rows)]
        for i in range(rows):
            PUM[i][i] = None
        FUV = function(PUM, PUV)
        for i in range(rows):
            self.assertFalse(FUV[i])
    def test_PUM_one_false_in_every_row(self):
        """Test when at least one element per row of PUM is False and all the PUV is True (to make the PUM matter),
        that all the FUV is False"""
        PUM = [
            [True, False, True, True, True, True, True, True, True, True, True, True, True, True, True],
            [False, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, False, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, False, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, False, True, True, True, True, True, True, True, True, True],
            
            [True, True, True, True, False, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, False, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, False, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, False, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, False, True, True, True, True, True, True],

            [True, True, True, True, True, True, True, True, True, True, True, False, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, False, True, False],
            [True, True, True, True, True, True, True, True, True, True, True, True, True, False, True],
        ]
        PUV = [True for _ in range(rows)]
        for i in range(rows):
            PUM[i][i] = None
        FUV = function(PUM, PUV)
        for i in range(rows):
            self.assertFalse(FUV[i])

    def test_general_PUM_and_PUV(self):
        """Test a general non specific example"""
        PUM = [
            [None, False, False, True, True, True, True, False, True, True, True, True, True, True, True],
            [False, None, True, False, True, True, True, True, True, True, True, True, True, True, True],
            [False, True, None, False, True, True, True, True, True, True, True, True, True, True, True],
            [True, False, False, None, False, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, False, None, True, True, True, True, True, True, True, True, True, True],
            
            [True, True, True, True, True, None, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, None, True, True, True, True, True, True, True, True],
            [False, True, True, True, True, True, True, None, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, None, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, None, True, True, True, True, True],

            [True, True, True, True, True, True, True, True, True, True, None, False, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, False, None, True, True, False],
            [True, True, True, True, True, True, True, True, True, True, True, True, None, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True, None, True],
            [True, True, True, True, True, True, True, True, True, True, True, False, True, True, None],
        ]
        PUV = [False, True, False, True, True, 
               True, True, True, False, False, 
               True, True, False, True, True]
        FUV_func = function(PUM,PUV)
        FUV_test = [True, False, True, False, False, 
                    True, True, False, True, True,
                    False, False, True, True, False]
        self.assertEqual(FUV_func, FUV_test)