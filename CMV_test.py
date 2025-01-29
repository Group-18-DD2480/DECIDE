import unittest

from CMV import *

class TestLIC_0(unittest.TestCase):
     # Tests for LIC0
    def test_LIC0_positive(self):
        # At least one pair with distance > LENGTH1
        X = [0,5,10]
        Y = [0,0,0]
        LENGTH1 = 4.0
        self.assertTrue(lic_0(X, Y, LENGTH1))

    def test_LIC0_negative1(self):
        # No pair with distance > LENGTH1
        X = [0,3,5]
        Y = [0,0,0]
        LENGTH1 = 6.0
        self.assertFalse(lic_0(X, Y, LENGTH1))

    def test_LIC0_negative2(self):
        # No pair with distance > LENGTH1
        X = [0,3,0]
        Y = [0,0,4]
        LENGTH1 = 5.0
        self.assertFalse(lic_0(X, Y, LENGTH1))


class TestLIC_1(unittest.TestCase):
    # Tests for LIC1
    def test_LIC1_positive(self):
        # A set of three points not contained within a circle of RADIUS1
        X = [0,1,0]
        Y = [0,0,3]
        RADIUS1 = 1.0
        self.assertTrue(lic_1(X, Y, RADIUS1))

    def test_LIC1_negative1(self):
        # All sets of three points are within a circle of RADIUS1
        X = [0,1,0]
        Y = [0,0,1]
        RADIUS1 = 2.0
        self.assertFalse(lic_1(X, Y, RADIUS1))

    def test_LIC1_negative2(self):
        # All sets of three points are within a circle of RADIUS1
        X = [0,2,0]
        Y = [0,0,2]
        RADIUS1 = 7.0
        self.assertFalse(lic_1(X, Y, RADIUS1))

class TestLIC_2(unittest.TestCase):
    # Tests for LIC2
    def test_LIC2_positive(self):
        # Angle less than (PI - EPSILON)
        X = [0,1,1]
        Y = [0,0,1]
        EPSILON = 0.0005
        self.assertTrue(lic_2(X, Y, EPSILON))

    def test_LIC2_negative(self):
        # Angle within (PI - EPSILON) and (PI + EPSILON)
        X = [0,1,2]
        Y = [0,0,0]
        EPSILON = 0.0005
        self.assertFalse(lic_2(X, Y, EPSILON))

    def test_LIC2_invalid_input(self):
        # Angle undefined due to coinciding points
        X = [0,0,1]
        Y = [0,0,1]
        EPSILON = 0.0005
        self.assertFalse(lic_2(X, Y, EPSILON))


class TestLIC_3(unittest.TestCase):
    # Tests for LIC3
    def test_LIC3_positive(self):
        # A triangle with area greater than AREA1
        X = [0,4,0]
        Y = [0,0,3]
        AREA1 = 5
        self.assertTrue(lic_3(X, Y, AREA1))

    def test_LIC3_negative(self):
        # No triangle with area greater than AREA1
        X = [0,1,0,0.5]
        Y = [0,0,1,0]
        AREA1 = 100
        self.assertFalse(lic_3(X, Y, AREA1))

    def test_LIC3_invalid_input(self):
        # Collinear points, area undefined (treated as 0)
        X = [0,1,2]
        Y = [0,1,2]
        AREA1 = 0.5
        self.assertFalse(lic_3(X, Y, AREA1))



    




class TestLIC_4(unittest.TestCase):
    def test_insufficient_points(self):
        (
            X,
            Y,
        ) = [0, 1, -1], [1, 3, 2]
        Q_PTS, QUADS = 4, 2
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_TRUE(self):
        (
            X,
            Y,
        ) = [1, -1, 1], [1, 3, 2]
        Q_PTS, QUADS = 3, 1
        self.assertTrue(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_FALSE(self):
        (
            X,
            Y,
        ) = [1, 4, 1], [1, 3, 2]
        Q_PTS, QUADS = 3, 1
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_PRIORITY_TRUE(self):
        (
            X,
            Y,
        ) = [0, -1, 1], [0, 0, 2]
        Q_PTS, QUADS = 3, 1
        self.assertTrue(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_PRIORITY_FALSE(self):
        (
            X,
            Y,
        ) = [0, 1, 0], [0, 0, 1]
        Q_PTS, QUADS = 3, 1
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_PRIORITY_ALL_I(self):
        (
            X,
            Y,
        ) = [0, 1, 0], [0, 0, 1]
        Q_PTS, QUADS = 3, 1
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_PRIORITY_ALL_II(self):
        (
            X,
            Y,
        ) = [-2, -1, -1], [1, 0, 1]
        Q_PTS, QUADS = 3, 1
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_PRIORITY_ALL_III(self):
        (
            X,
            Y,
        ) = [0, -1, -1], [-1, -2, -1]
        Q_PTS, QUADS = 3, 1
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_PRIORITY_ALL_IV(self):
        (
            X,
            Y,
        ) = [1, 2, 4], [-1, -3, -1]
        Q_PTS, QUADS = 3, 1
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))


class TestLIC_5(unittest.TestCase):
    def test_insufficient_points(self):
        X, Y = [0], [1]
        self.assertFalse(lic_5(X, Y))

    def test_second_X_smaller(self):
        X, Y = [0, -2], [1, 1]
        self.assertTrue(lic_5(X, Y))

    def test_second_X_larger(self):
        X, Y = [0, 2], [1, 1]
        self.assertFalse(lic_5(X, Y))


class TestLIC_6(unittest.TestCase):
    def test_insufficient_points(self):
        X = [0, 1, 2]
        Y = [0, 1, 0]
        N_PTS, DIST = 4, 1
        self.assertFalse(lic_6(X, Y, N_PTS, DIST))

    def test_coincident_point_true(self):
        X = [0, 10, 1, 0]
        Y = [0, 10, 0, 0]
        N_PTS, DIST = 4, 2
        self.assertTrue(lic_6(X, Y, N_PTS, DIST))

    def test_coincident_point_false(self):
        X = [0, 0, 1, 0]
        Y = [0, 1, 0, 0]
        N_PTS, DIST = 4, 2
        self.assertFalse(lic_6(X, Y, N_PTS, DIST))

    def test_diff_point_true(self):
        X = [0, 0, 0, 10]
        Y = [0, 10, 0, 0]
        N_PTS, DIST = 4, 2
        self.assertTrue(lic_6(X, Y, N_PTS, DIST))

    def test_diff_point_false(self):
        X = [0, 0, 1, 10]
        Y = [0, 1, 0, 0]
        N_PTS, DIST = 4, 2
        self.assertFalse(lic_6(X, Y, N_PTS, DIST))

class TestLIC_7(unittest.TestCase):
    def test_insufficient_points(self):
        X, Y = [0, 1], [0, 1]
        K_PTS, LENGTH1 = 1, 1
        self.assertFalse(lic_7(X, Y, K_PTS, LENGTH1))

    def test_distance_greater(self):
        X, Y = [0, 1, 2, 5], [0, 1, 2, 5]
        K_PTS, LENGTH1 = 1, 3
        self.assertTrue(lic_7(X, Y, K_PTS, LENGTH1))

    def test_distance_smaller(self):
        X, Y = [0, 1, 2, 3], [0, 1, 2, 3]
        K_PTS, LENGTH1 = 1, 5
        self.assertFalse(lic_7(X, Y, K_PTS, LENGTH1))


class TestLIC_8(unittest.TestCase):
    def test_insufficient_points(self):
        X, Y = [0, 1, 2, 3], [0, 1, 2, 3]
        A_PTS, B_PTS, RADIUS1 = 1, 1, 1
        self.assertFalse(lic_8(X, Y, A_PTS, B_PTS, RADIUS1))

    def test_points_outside_circle(self):
        X, Y = [0, 1, 2, 3, 10, 6], [0, 1, 2, 3, 10, 6]
        A_PTS, B_PTS, RADIUS1 = 1, 1, 3
        self.assertTrue(lic_8(X, Y, A_PTS, B_PTS, RADIUS1))

    def test_points_inside_circle(self):
        X, Y = [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]
        A_PTS, B_PTS, RADIUS1 = 1, 1, 10
        self.assertFalse(lic_8(X, Y, A_PTS, B_PTS, RADIUS1))


class TestLIC_9(unittest.TestCase):
    def test_insufficient_points(self):
        X, Y = [0, 1, 2, 3], [0, 1, 2, 3]
        C_PTS, D_PTS, EPSILON = 1, 1, 0.1
        self.assertFalse(lic_9(X, Y, C_PTS, D_PTS, EPSILON))

    def test_angle_outside_bounds(self):
        # Points that form a clear acute angle (~45°) with valid spacing:
        # First point at (0,0), vertex at (2,2), last point at (4,2)
        # With C_PTS=1 and D_PTS=1, this ensures correct point separation
        X = [0, 1, 2, 3, 4]
        Y = [0, 1, 2, 2, 2]
        C_PTS, D_PTS, EPSILON = 1, 1, 0.1
        self.assertTrue(lic_9(X, Y, C_PTS, D_PTS, EPSILON))

    def test_angle_within_bounds(self):
        # Points that form ~180° angle (within PI±EPSILON)
        X = [-2, 1, 0, 1, 2]
        Y = [0, 1, 0, -1, 0]
        C_PTS, D_PTS, EPSILON = 1, 1, 0.1
        self.assertFalse(lic_9(X, Y, C_PTS, D_PTS, EPSILON))

    def test_coincident_points(self):
        # Point coincides with vertex
        X = [1, 0, 2, 0, 2]
        Y = [1, 0, 2, 2, 2]
        C_PTS, D_PTS, EPSILON = 1, 1, 0.1
        self.assertFalse(lic_9(X, Y, C_PTS, D_PTS, EPSILON))

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

    def test_both_condition_met(self):
        X, Y = [0, 0, 5, 6, 10], [0, 1, 5, 4, 0]
        E_PTS, F_PTS, AREA1, AREA2 = 1, 1, 10.0, 40.0
        self.assertTrue(lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2))

    def test_no_conditions_met(self):
        X, Y = [0, 5, 1, 5, 2], [0, 3, 1, 4, 0]
        E_PTS, F_PTS, AREA1, AREA2 = 1, 1, 15.0, 10.0
        self.assertFalse(lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2))

    def test_only_condition_1_met(self):
        X, Y = [0, 0, 5, 6, 10], [0, 1, 5, 4, 0]
        E_PTS, F_PTS, AREA1, AREA2 = 1, 1, 10.0, 20.0
        self.assertFalse(lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2))

    def test_only_condition_2_met(self):
        X, Y = [0, 0, 5, 6, 10], [0, 1, 5, 4, 0]
        E_PTS, F_PTS, AREA1, AREA2 = 1, 1, 30.0, 40.0
        self.assertFalse(lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2))
if __name__ == '__main__':
    unittest.main()