import unittest
from CMV import *

class TestLIC_13(unittest.TestCase):
    def test_insufficient_points(self):
        X, Y = [0, 1], [0, 1]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 1.0, 2.0
        self.assertFalse(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))

    def test_radius_condition_met(self):
        X, Y = [0, 0, 5 , 6, 10], [0, 1, 5, 6,  0]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 4.0, 15.0
        self.assertTrue(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))

    def test_radius_condition_not_met(self):
        X, Y = [0, 0, 5 , 6, 10], [0, 1, 5, 6,  0]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 6.0, 1.0
        self.assertFalse(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))

    def test_radius_condition_met_inline(self):
        X, Y = [0, 1, 0 , 6, 0], [0, 1, 5, 6,  10]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 4.0, 15.0
        self.assertTrue(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))

    def test_radius_condition_not_met_inline(self):
        X, Y = [0, 1, 0 , 6, 0], [0, 1, 5, 6,  10]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 5.0, 1.0
        self.assertFalse(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))
    
    def test_fail_radiusA_only(self):
        X, Y = [0, 0, 5 , 6, 10], [0, 1, 5, 6,  0]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 5.0, 15.0
        self.assertFalse(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))
    
    
    def test_fail_radiusB_only(self):
        X, Y = [0, 0, 5 , 6, 10], [0, 1, 5, 6,  0]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 4.0, 1.0
        self.assertFalse(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))
        
if __name__ == "__main__":
    unittest.main()