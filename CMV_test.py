import unittest

from CMV import lic_10, lic_11, lic_12
from CMV import lic_7, lic_8
from CMV import lic_4, lic_5, lic_6


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


if __name__ == "__main__":
    unittest.main()
