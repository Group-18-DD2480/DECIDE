import unittest

from src.CMV import (
    lic_0,
    lic_1,
    lic_2,
    lic_3,
    lic_4,
    lic_5,
    lic_6,
    lic_7,
    lic_8,
    lic_9,
    lic_10,
    lic_11,
    lic_12,
    lic_13,
    lic_14,
)


class TestLIC_0(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #0.

    Condition: There exists at least one set of two consecutive data points that are a
    distance greater than the length, LENGTH1, apart.
    """

    def test_LIC0_positive(self):
        """Test when two consecutive points are further than LENGTH1 apart."""
        # At least one pair with distance > LENGTH1
        X = [0, 5, 10]
        Y = [0, 0, 0]
        LENGTH1 = 4.0
        self.assertTrue(lic_0(X, Y, LENGTH1))

    def test_LIC0_negative1(self):
        """Test when no consecutive points are further than LENGTH1 apart."""
        # No pair with distance > LENGTH1
        X = [0, 3, 5]
        Y = [0, 0, 0]
        LENGTH1 = 6.0
        self.assertFalse(lic_0(X, Y, LENGTH1))

    def test_LIC0_negative2(self):
        """Test when points are arranged diagonally but still within LENGTH1."""
        # No pair with distance > LENGTH1
        X = [0, 3, 0]
        Y = [0, 0, 4]
        LENGTH1 = 5.0
        self.assertFalse(lic_0(X, Y, LENGTH1))


class TestLIC_1(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #1.

    Condition: There exists at least one set of three consecutive data points that
    cannot all be contained within or on a circle of radius RADIUS1.
    """

    def test_LIC1_positive(self):
        """Test when three consecutive points cannot be contained in circle of RADIUS1."""
        # A set of three points not contained within a circle of RADIUS1
        X = [0, 1, 0]
        Y = [0, 0, 3]
        RADIUS1 = 1.0
        self.assertTrue(lic_1(X, Y, RADIUS1))

    def test_LIC1_negative1(self):
        """Test when all points can be contained within circle of RADIUS1."""
        # All sets of three points are within a circle of RADIUS1
        X = [0, 1, 0]
        Y = [0, 0, 1]
        RADIUS1 = 2.0
        self.assertFalse(lic_1(X, Y, RADIUS1))

    def test_LIC1_negative2(self):
        """Test with larger RADIUS1 that can contain all points."""
        # All sets of three points are within a circle of RADIUS1
        X = [0, 2, 0]
        Y = [0, 0, 2]
        RADIUS1 = 7.0
        self.assertFalse(lic_1(X, Y, RADIUS1))


class TestLIC_2(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #2.

    Condition: There exists at least one set of three consecutive data points which form an angle
    such that angle < (PI - EPSILON) or angle > (PI + EPSILON). The second point is the vertex.
    """

    def test_LIC2_positive(self):
        """Test when angle is less than (PI - EPSILON)."""
        # Angle less than (PI - EPSILON)
        X = [0, 1, 1]
        Y = [0, 0, 1]
        EPSILON = 0.0005
        self.assertTrue(lic_2(X, Y, EPSILON))

    def test_LIC2_negative(self):
        """Test when angle is within bounds."""
        # Angle within (PI - EPSILON) and (PI + EPSILON)
        X = [0, 1, 2]
        Y = [0, 0, 0]
        EPSILON = 0.0005
        self.assertFalse(lic_2(X, Y, EPSILON))

    def test_LIC2_invalid_input(self):
        """Test when angle is undefined due to coinciding points."""
        # Angle undefined due to coinciding points
        X = [0, 0, 1]
        Y = [0, 0, 1]
        EPSILON = 0.0005
        self.assertFalse(lic_2(X, Y, EPSILON))


class TestLIC_3(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #3.

    Condition: There exists at least one set of three consecutive data points that form
    a triangle with area greater than AREA1.
    """

    def test_LIC3_positive(self):
        """Test when triangle area is greater than AREA1."""
        # A triangle with area greater than AREA1
        X = [0, 4, 0]
        Y = [0, 0, 3]
        AREA1 = 5
        self.assertTrue(lic_3(X, Y, AREA1))

    def test_LIC3_negative(self):
        """Test when no triangle has area greater than AREA1."""
        # No triangle with area greater than AREA1
        X = [0, 1, 0, 0.5]
        Y = [0, 0, 1, 0]
        AREA1 = 100
        self.assertFalse(lic_3(X, Y, AREA1))

    def test_LIC3_invalid_input(self):
        """Test when points are collinear (area = 0)."""
        # Collinear points, area undefined (treated as 0)
        X = [0, 1, 2]
        Y = [0, 1, 2]
        AREA1 = 0.5
        self.assertFalse(lic_3(X, Y, AREA1))


class TestLIC_4(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #4.

    Condition: There exists at least one set of Q_PTS consecutive data points that lie
    in more than QUADS different quadrants.
    """

    def test_insufficient_points(self):
        """Test when there are fewer points than Q_PTS."""
        (
            X,
            Y,
        ) = [0, 1, -1], [1, 3, 2]
        Q_PTS, QUADS = 4, 2
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_TRUE(self):
        """Test when points lie in more than QUADS quadrants."""
        (
            X,
            Y,
        ) = [1, -1, 1], [1, 3, 2]
        Q_PTS, QUADS = 3, 1
        self.assertTrue(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_FALSE(self):
        """Test when points do not lie in more than QUADS quadrants."""
        (
            X,
            Y,
        ) = [1, 4, 1], [1, 3, 2]
        Q_PTS, QUADS = 3, 1
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_PRIORITY_TRUE(self):
        """Test when points lie in more than QUADS quadrants with priority."""
        (
            X,
            Y,
        ) = [0, -1, 1], [0, 0, 2]
        Q_PTS, QUADS = 3, 1
        self.assertTrue(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_PRIORITY_FALSE(self):
        """Test when points do not lie in more than QUADS quadrants with priority."""
        (
            X,
            Y,
        ) = [0, 1, 0], [0, 0, 1]
        Q_PTS, QUADS = 3, 1
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_PRIORITY_ALL_I(self):
        """Test when all points lie in the first quadrant."""
        (
            X,
            Y,
        ) = [0, 1, 0], [0, 0, 1]
        Q_PTS, QUADS = 3, 1
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_PRIORITY_ALL_II(self):
        """Test when all points lie in the second quadrant."""
        (
            X,
            Y,
        ) = [-2, -1, -1], [1, 0, 1]
        Q_PTS, QUADS = 3, 1
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_PRIORITY_ALL_III(self):
        """Test when all points lie in the third quadrant."""
        (
            X,
            Y,
        ) = [0, -1, -1], [-1, -2, -1]
        Q_PTS, QUADS = 3, 1
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))

    def test_1QUADS_PRIORITY_ALL_IV(self):
        """Test when all points lie in the fourth quadrant."""
        (
            X,
            Y,
        ) = [1, 2, 4], [-1, -3, -1]
        Q_PTS, QUADS = 3, 1
        self.assertFalse(lic_4(X, Y, Q_PTS, QUADS))


class TestLIC_5(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #5.

    Condition: There exists at least one set of two consecutive data points such that
    X[j] - X[i] < 0 (where i < j).
    """

    def test_insufficient_points(self):
        """Test when there are fewer than two points."""
        X, Y = [0], [1]
        self.assertFalse(lic_5(X, Y))

    def test_second_X_smaller(self):
        """Test when the second point's X is smaller than the first."""
        X, Y = [0, -2], [1, 1]
        self.assertTrue(lic_5(X, Y))

    def test_second_X_larger(self):
        """Test when the second point's X is larger than the first."""
        X, Y = [0, 2], [1, 1]
        self.assertFalse(lic_5(X, Y))


class TestLIC_6(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #6.

    Condition: There exists at least one set of N_PTS consecutive data points such that
    at least one of the points lies a distance greater than DIST from the line joining
    the first and last of these N_PTS points.
    """

    def test_insufficient_points(self):
        """Test when there are fewer points than N_PTS."""
        X = [0, 1, 2]
        Y = [0, 1, 0]
        N_PTS, DIST = 4, 1
        self.assertFalse(lic_6(X, Y, N_PTS, DIST))

    def test_coincident_point_true(self):
        """Test when a point lies further than DIST from the line."""
        X = [0, 10, 1, 0]
        Y = [0, 10, 0, 0]
        N_PTS, DIST = 4, 2
        self.assertTrue(lic_6(X, Y, N_PTS, DIST))

    def test_coincident_point_false(self):
        """Test when no point lies further than DIST from the line."""
        X = [0, 0, 1, 0]
        Y = [0, 1, 0, 0]
        N_PTS, DIST = 4, 2
        self.assertFalse(lic_6(X, Y, N_PTS, DIST))

    def test_diff_point_true(self):
        """Test when a point lies further than DIST from the line."""
        X = [0, 0, 0, 10]
        Y = [0, 10, 0, 0]
        N_PTS, DIST = 4, 2
        self.assertTrue(lic_6(X, Y, N_PTS, DIST))

    def test_diff_point_false(self):
        """Test when no point lies further than DIST from the line."""
        X = [0, 0, 1, 10]
        Y = [0, 1, 0, 0]
        N_PTS, DIST = 4, 2
        self.assertFalse(lic_6(X, Y, N_PTS, DIST))


class TestLIC_7(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #7.

    Condition: There exists at least one set of two data points separated by exactly K_PTS
    consecutive intervening points that are a distance greater than the length, LENGTH1, apart.
    """

    def test_insufficient_points(self):
        """Test when there are fewer points than required."""
        X, Y = [0, 1], [0, 1]
        K_PTS, LENGTH1 = 1, 1
        self.assertFalse(lic_7(X, Y, K_PTS, LENGTH1))

    def test_distance_greater(self):
        """Test when the distance between points is greater than LENGTH1."""
        X, Y = [0, 1, 2, 5], [0, 1, 2, 5]
        K_PTS, LENGTH1 = 1, 3
        self.assertTrue(lic_7(X, Y, K_PTS, LENGTH1))

    def test_distance_smaller(self):
        """Test when the distance between points is smaller than LENGTH1."""
        X, Y = [0, 1, 2, 3], [0, 1, 2, 3]
        K_PTS, LENGTH1 = 1, 5
        self.assertFalse(lic_7(X, Y, K_PTS, LENGTH1))


class TestLIC_8(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #8.

    Condition: There exists at least one set of three data points separated by exactly A_PTS
    and B_PTS consecutive intervening points, respectively, that cannot all be contained
    within or on a circle of radius RADIUS1.
    """

    def test_insufficient_points(self):
        """Test when there are fewer points than required."""
        X, Y = [0, 1, 2, 3], [0, 1, 2, 3]
        A_PTS, B_PTS, RADIUS1 = 1, 1, 1
        self.assertFalse(lic_8(X, Y, A_PTS, B_PTS, RADIUS1))

    def test_points_outside_circle(self):
        """Test when points cannot be contained within a circle of RADIUS1."""
        X, Y = [0, 1, 2, 3, 10, 6], [0, 1, 2, 3, 10, 6]
        A_PTS, B_PTS, RADIUS1 = 1, 1, 3
        self.assertTrue(lic_8(X, Y, A_PTS, B_PTS, RADIUS1))

    def test_points_inside_circle(self):
        """Test when points can be contained within a circle of RADIUS1."""
        X, Y = [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]
        A_PTS, B_PTS, RADIUS1 = 1, 1, 10
        self.assertFalse(lic_8(X, Y, A_PTS, B_PTS, RADIUS1))


class TestLIC_9(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #9.

    Condition: There exists at least one set of three data points separated by exactly C_PTS
    and D_PTS consecutive intervening points, respectively, that form an angle such that
    angle < (PI - EPSILON) or angle > (PI + EPSILON). The second point is the vertex.
    """

    def test_insufficient_points(self):
        """Test when there are fewer points than required."""
        X, Y = [0, 1, 2, 3], [0, 1, 2, 3]
        C_PTS, D_PTS, EPSILON = 1, 1, 0.1
        self.assertFalse(lic_9(X, Y, C_PTS, D_PTS, EPSILON))

    def test_angle_outside_bounds(self):
        """Test when the angle is outside the bounds (PI - EPSILON) and (PI + EPSILON)."""
        # Points that form a clear acute angle (~45°) with valid spacing:
        # First point at (0,0), vertex at (2,2), last point at (4,2)
        # With C_PTS=1 and D_PTS=1, this ensures correct point separation
        X = [0, 1, 2, 3, 4]
        Y = [0, 1, 2, 2, 2]
        C_PTS, D_PTS, EPSILON = 1, 1, 0.1
        self.assertTrue(lic_9(X, Y, C_PTS, D_PTS, EPSILON))

    def test_angle_within_bounds(self):
        """Test when the angle is within the bounds (PI - EPSILON) and (PI + EPSILON)."""
        # Points that form ~180° angle (within PI±EPSILON)
        X = [-2, 1, 0, 1, 2]
        Y = [0, 1, 0, -1, 0]
        C_PTS, D_PTS, EPSILON = 1, 1, 0.1
        self.assertFalse(lic_9(X, Y, C_PTS, D_PTS, EPSILON))

    def test_coincident_points(self):
        """Test when points coincide with the vertex."""
        # Point coincides with vertex
        X = [1, 0, 2, 0, 2]
        Y = [1, 0, 2, 2, 2]
        C_PTS, D_PTS, EPSILON = 1, 1, 0.1
        self.assertFalse(lic_9(X, Y, C_PTS, D_PTS, EPSILON))


class TestLIC_10(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #10.

    Condition: There exists at least one set of three data points separated by exactly E_PTS
    and F_PTS consecutive intervening points, respectively, that form a triangle with area
    greater than AREA1.
    """

    def test_insufficient_points(self):
        """Test when there are fewer points than required."""
        X, Y = [0, 1, 2], [0, 1, 0]
        E_PTS, F_PTS, AREA1 = 1, 1, 1
        self.assertFalse(lic_10(X, Y, E_PTS, F_PTS, AREA1))

    def test_area_greater(self):
        """Test when the triangle area is greater than AREA1."""
        X, Y = [0, 1, 2, 3, 4], [0, 1, 2, 1, 5]
        E_PTS, F_PTS, AREA1 = 1, 1, 0.5
        self.assertTrue(lic_10(X, Y, E_PTS, F_PTS, AREA1))

    def test_area_smaller(self):
        """Test when the triangle area is smaller than AREA1."""
        X, Y = [0, 1, 2, 3, 4], [0, 1, 1, 1, 0]
        E_PTS, F_PTS, AREA1 = 1, 1, 2
        self.assertFalse(lic_10(X, Y, E_PTS, F_PTS, AREA1))


class TestLIC_11(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #11.

    Condition: There exists at least one set of two data points separated by exactly G_PTS
    consecutive intervening points such that X[j] - X[i] < 0 (where i < j).
    """

    def test_insufficient_points(self):
        """Test when there are fewer points than required."""
        X, G_PTS = [0, 1], 1
        self.assertFalse(lic_11(X, G_PTS))

    def test_difference_positive(self):
        """Test when the difference X[j] - X[i] is positive."""
        X, G_PTS = [0, 1, 2, 3, 4, 5], 1
        self.assertFalse(lic_11(X, G_PTS))

    def test_difference_negative(self):
        """Test when the difference X[j] - X[i] is negative."""
        X, G_PTS = [5, 4, 3, 2, 1, 0], 1
        self.assertTrue(lic_11(X, G_PTS))


class TestLIC_12(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #12.

    Condition: There exists at least one set of two data points separated by exactly K_PTS
    consecutive intervening points that are a distance greater than the length, LENGTH1, apart.
    In addition, there exists at least one set of two data points separated by exactly K_PTS
    consecutive intervening points that are a distance less than the length, LENGTH2, apart.
    """

    def test_insufficient_points(self):
        """Test when there are fewer points than required."""
        X, Y = [0, 1], [0, 1]
        K_PTS, LENGTH1, LENGTH2 = 1, 1, 2
        self.assertFalse(lic_12(X, Y, K_PTS, LENGTH1, LENGTH2))

    def test_only_g(self):
        """Test when only the greater distance condition is met."""
        X, Y = [0, 3, 0, 3], [0, 0, 3, 3]
        K_PTS, LENGTH1, LENGTH2 = 1, 2, 0.5
        self.assertFalse(lic_12(X, Y, K_PTS, LENGTH1, LENGTH2))

    def test_only_l(self):
        """Test when only the lesser distance condition is met."""
        X, Y = [0, 1, 0, 1], [0, 0, 1, 1]
        K_PTS, LENGTH1, LENGTH2 = 1, 5, 1.5
        self.assertFalse(lic_12(X, Y, K_PTS, LENGTH1, LENGTH2))

    def test_both(self):
        """Test when both distance conditions are met."""
        X, Y = [0, 10, 0, 1, 15, 2], [0, 10, 0, 1, 15, 2]
        K_PTS, LENGTH1, LENGTH2 = 1, 8, 2
        self.assertTrue(lic_12(X, Y, K_PTS, LENGTH1, LENGTH2))


class TestLIC_13(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #13.

    Condition: There exists at least one set of three data points separated by exactly A_PTS
    and B_PTS consecutive intervening points, respectively, that cannot all be contained
    within or on a circle of radius RADIUS1. In addition, there exists at least one set of
    three data points separated by exactly A_PTS and B_PTS consecutive intervening points,
    respectively, that can all be contained within or on a circle of radius RADIUS2.
    """

    def test_insufficient_points(self):
        """Test when there are fewer points than required."""
        X, Y = [0, 1], [0, 1]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 1.0, 2.0
        self.assertFalse(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))

    def test_radius_condition_met(self):
        """Test when both radius conditions are met."""
        X, Y = [0, 0, 5, 6, 10], [0, 1, 5, 6, 0]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 4.0, 15.0
        self.assertTrue(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))

    def test_radius_condition_not_met(self):
        """Test when neither radius condition is met."""
        X, Y = [0, 0, 5, 6, 10], [0, 1, 5, 6, 0]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 6.0, 1.0
        self.assertFalse(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))

    def test_radius_condition_met_inline(self):
        """Test when both radius conditions are met with inline points."""
        X, Y = [0, 1, 0, 6, 0], [0, 1, 5, 6, 10]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 4.0, 15.0
        self.assertTrue(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))

    def test_radius_condition_not_met_inline(self):
        """Test when neither radius condition is met with inline points."""
        X, Y = [0, 1, 0, 6, 0], [0, 1, 5, 6, 10]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 5.0, 1.0
        self.assertFalse(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))

    def test_fail_radiusA_only(self):
        """Test when only the first radius condition is not met."""
        X, Y = [0, 0, 5, 6, 10], [0, 1, 5, 6, 0]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 5.0, 15.0
        self.assertFalse(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))

    def test_fail_radiusB_only(self):
        """Test when only the second radius condition is not met."""
        X, Y = [0, 0, 5, 6, 10], [0, 1, 5, 6, 0]
        A_PTS, B_PTS, RADIUS1, RADIUS2 = 1, 1, 4.0, 1.0
        self.assertFalse(lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2))


class TestLIC_14(unittest.TestCase):
    """Test suite for Launch Interceptor Condition #14.

    Condition: There exists at least one set of three data points separated by exactly E_PTS
    and F_PTS consecutive intervening points, respectively, that form a triangle with area
    greater than AREA1. In addition, there exists at least one set of three data points
    separated by exactly E_PTS and F_PTS consecutive intervening points, respectively, that
    form a triangle with area less than AREA2.
    """

    def test_insufficient_points(self):
        """Test when there are fewer points than required."""
        X, Y = [0, 1], [0, 1]
        E_PTS, F_PTS, AREA1, AREA2 = 1, 1, 1.0, 2.0
        self.assertFalse(lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2))

    def test_both_condition_met(self):
        """Test when both area conditions are met."""
        X, Y = [0, 0, 5, 6, 10], [0, 1, 5, 4, 0]
        E_PTS, F_PTS, AREA1, AREA2 = 1, 1, 10.0, 40.0
        self.assertTrue(lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2))

    def test_no_conditions_met(self):
        """Test when neither area condition is met."""
        X, Y = [0, 5, 1, 5, 2], [0, 3, 1, 4, 0]
        E_PTS, F_PTS, AREA1, AREA2 = 1, 1, 15.0, 10.0
        self.assertFalse(lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2))

    def test_only_condition_1_met(self):
        """Test when only the first area condition is met."""
        X, Y = [0, 0, 5, 6, 10], [0, 1, 5, 4, 0]
        E_PTS, F_PTS, AREA1, AREA2 = 1, 1, 10.0, 20.0
        self.assertFalse(lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2))

    def test_only_condition_2_met(self):
        """Test when only the second area condition is met."""
        X, Y = [0, 0, 5, 6, 10], [0, 1, 5, 4, 0]
        E_PTS, F_PTS, AREA1, AREA2 = 1, 1, 30.0, 40.0
        self.assertFalse(lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2))


if __name__ == "__main__":
    unittest.main()
