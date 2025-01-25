import decide as DECIDE
import math

def distance(px1, py1, px2, py2) -> bool:
    return math.sqrt(math.pow(px1 - px2, 2) + math.pow(py1 - py2, 2))


def lic_0() -> bool:
    for i in range(DECIDE.NUMPOINTS - 1):
        if distance(DECIDE.X[i], DECIDE.Y[i], DECIDE.X[i+1], DECIDE.Y[i+1]) > DECIDE.PARAMETERS.LENGTH1:
            return True
        
    return False # no such set of points exists


def lic_1() -> bool:
    def circumcircle_radius(px1, py1, px2, py2, px3, py3):
        # Calculate pairwise distances
        a = distance(px1, py1, px2, py2)
        b = distance(px1, py1, px3, py3)
        c = distance(px2, py2, px3, py3)

        # Semi-perimeter
        s = (a + b + c) / 2

        # Area of the triangle using Heron's formula
        try:
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        except ValueError:
            return float('inf')

        # Circumcircle radius formula: R = (abc) / (4 * area)
        if area == 0:
            return float('inf')  # Points are collinear

        R = (a * b * c) / (4 * area)
        return R
    
    for i in range(DECIDE.NUMPOINTS - 2):
        R = circumcircle_radius(DECIDE.X[i], DECIDE.Y[i], DECIDE.X[i+1], DECIDE.Y[i+1], DECIDE.X[i+2], DECIDE.Y[i+2])
        if R > DECIDE.PARAMETERS.RADIUS1:
            return True
    return False # no such set of points exists