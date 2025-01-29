import decide as DECIDE
import unittest


def setup_DECIDE(points, parameters):
    DECIDE.POINTS = points
    DECIDE.NUMPOINTS = len(points)
    DECIDE.PARAMETERS = parameters

class TestLICs(unittest.TestCase):
    # Tests for LIC0
    def test_LIC0_positive(self):
        # At least one pair with distance > LENGTH1
        points = [(0, 0), (5, 0), (10, 0)]
        parameters = {'LENGTH1': 4}
        setup_DECIDE(points, parameters)
        self.assertTrue(DECIDE.LIC0())

    def test_LIC0_negative1(self):
        # No pair with distance > LENGTH1
        points = [(0, 0), (3, 0), (5, 0)]
        parameters = {'LENGTH1': 6}
        setup_DECIDE(points, parameters)
        self.assertFalse(DECIDE.LIC0())

    def test_LIC0_negative2(self):
        # No pair with distance > LENGTH1
        points = [(0, 0), (3, 0), (0, 4)]
        parameters = {'LENGTH1': 5}
        setup_DECIDE(points, parameters)
        self.assertFalse(DECIDE.LIC0())

    # Tests for LIC1
    def test_LIC1_positive(self):
        # A set of three points not contained within a circle of RADIUS1
        points = [(0, 0), (1, 0), (0, 3)]
        parameters = {'RADIUS1': 1.0}
        setup_DECIDE(points, parameters)
        self.assertTrue(DECIDE.LIC1())

    def test_LIC1_negative1(self):
        # All sets of three points are within a circle of RADIUS1
        points = [(0, 0), (1, 0), (0, 1)]
        parameters = {'RADIUS1': 2.0}
        setup_DECIDE(points, parameters)
        self.assertFalse(DECIDE.LIC1())

    def test_LIC1_negative2(self):
        # All sets of three points are within a circle of RADIUS1
        points = [(0, 0), (2, 0), (0, 2)]
        parameters = {'RADIUS1': 7}
        setup_DECIDE(points, parameters)
        self.assertFalse(DECIDE.LIC1())

    # Tests for LIC2
    def test_LIC2_positive(self):
        # Angle less than (PI - EPSILON)
        points = [(0, 0), (1, 0), (1, 1)]
        parameters = {'EPSILON': 0.0005}
        setup_DECIDE(points, parameters)
        self.assertTrue(DECIDE.LIC2())

    def test_LIC2_negative(self):
        # Angle within (PI - EPSILON) and (PI + EPSILON)
        points = [(0, 0), (1, 0), (2, 0)]
        parameters = {'EPSILON': 0.0005}
        setup_DECIDE(points, parameters)
        self.assertFalse(DECIDE.LIC2())

    def test_LIC2_invalid_input(self):
        # Angle undefined due to coinciding points
        points = [(0, 0), (0, 0), (1, 1)]
        parameters = {'EPSILON': 0.0005}
        setup_DECIDE(points, parameters)
        self.assertFalse(DECIDE.LIC2())


    # Tests for LIC3
    def test_LIC3_positive(self):
        # A triangle with area greater than AREA1
        points = [(0, 0), (4, 0), (0, 3)]
        parameters = {'AREA1': 5}
        setup_DECIDE(points, parameters)
        self.assertTrue(DECIDE.LIC3())

    def test_LIC3_negative(self):
        # No triangle with area greater than AREA1
        points = [(0, 0), (1, 0), (0, 1)]
        parameters = {'AREA1': 1}
        setup_DECIDE(points, parameters)
        self.assertFalse(DECIDE.LIC3())

    def test_LIC3_invalid_input(self):
        # Collinear points, area undefined (treated as 0)
        points = [(0, 0), (1, 1), (2, 2)]
        parameters = {'AREA1': 0.5}
        setup_DECIDE(points, parameters)
        self.assertFalse(DECIDE.LIC3())

if __name__ == '__main__':
    unittest.main()