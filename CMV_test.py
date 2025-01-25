import unittest
from CMV import *

class TestLIC_10(unittest.TestCase):
    def test_insufficient_points(self):
        X, Y = [0, 1, 2], [0, 1, 0]
        E_PTS, F_PTS, AREA1 = 1, 1, 1
        self.assertFalse(lic_10(X, Y, E_PTS, F_PTS, AREA1))
        
    def test_area_greater(self):
        X, Y = [0, 1, 2, 3, 4], [0, 1, 2, 1, 5]
        E_PTS, F_PTS, AREA1 = 1, 1, 0.5
        self.assertTrue(lic_10(X, Y, E_PTS, F_PTS, AREA1))
        
    def test_area_smaller(self):
        X, Y = [0, 1, 2, 3, 4], [0, 1, 1, 1, 0]
        E_PTS, F_PTS, AREA1 = 1, 1, 2
        self.assertFalse(lic_10(X, Y, E_PTS, F_PTS, AREA1))


class TestLIC_11(unittest.TestCase):
    def test_insufficient_points(self):
        X, G_PTS = [0, 1], 1
        self.assertFalse(lic_11(X, G_PTS))
        
    def test_difference_positive(self):
        X, G_PTS = [0, 1, 2, 3, 4, 5], 1
        self.assertFalse(lic_11(X, G_PTS))
    
    def test_difference_negative(self):
        X, G_PTS = [5, 4, 3, 2, 1, 0], 1
        self.assertTrue(lic_11(X, G_PTS))


class TestLIC_12(unittest.TestCase):
    def test_insufficient_points(self):
        X, Y = [0, 1], [0, 1]
        K_PTS, LENGTH1, LENGTH2 = 1, 1, 2
        self.assertFalse(lic_12(X, Y, K_PTS, LENGTH1, LENGTH2))
        
    def test_only_g(self):
        X, Y = [0, 3, 0, 3], [0, 0, 3, 3]
        K_PTS, LENGTH1, LENGTH2 = 1, 2, 0.5
        self.assertFalse(lic_12(X, Y, K_PTS, LENGTH1, LENGTH2))

    def test_only_l(self):
        X, Y = [0, 1, 0, 1], [0, 0, 1, 1]
        K_PTS, LENGTH1, LENGTH2 = 1, 5, 1.5
        self.assertFalse(lic_12(X, Y, K_PTS, LENGTH1, LENGTH2))

    def test_both(self):
        X, Y = [0, 10, 0, 1, 15, 2], [0, 0, 10, 1, 15, 2]
        K_PTS, LENGTH1, LENGTH2 = 1, 8, 2
        self.assertTrue(lic_12(X, Y, K_PTS, LENGTH1, LENGTH2))
        
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
        
class TestLIC_14(unittest.TestCase):
    def test_insufficient_points(self):
        X, Y = [0, 1], [0, 1]
        E_PTS, F_PTS, AREA1, AREA2 = 1, 1, 1.0, 2.0
        self.assertFalse(lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2))

    def test_area_condition_met(self):
        X, Y = [0, 0, 5, 6, 10], [0, 1, 5, 4, 0]
        E_PTS, F_PTS, AREA1, AREA2 = 1, 1, 10.0, 20.0
        self.assertTrue(lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2))

    def test_area_condition_not_met(self):
        X, Y = [0, 5, 1, 5, 2], [0, 3, 1, 4, 0]
        E_PTS, F_PTS, AREA1, AREA2 = 1, 1, 15.0, 10.0
        self.assertFalse(lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2))
        
if __name__ == '__main__':
    unittest.main()