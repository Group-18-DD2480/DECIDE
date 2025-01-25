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


def lic_2():
    def angle_between_vectors(v1, v2):
        dot_product = v1[0] * v2[0] + v1[1] * v2[1]
        magnitude_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
        magnitude_v2 = math.sqrt(v2[0]**2 + v2[1]**2)

        # Avoid division by zero
        if magnitude_v1 == 0 or magnitude_v2 == 0:
            raise ValueError("One or both vectors have zero magnitude.")

        cos_theta = dot_product / (magnitude_v1 * magnitude_v2)
        cos_theta = max(-1, min(1, cos_theta))  # Clamp value to avoid numerical errors

        return math.acos(cos_theta)
    
    for i in range(DECIDE.NUMPOINTS - 2):
        p1, p2, p3 = (DECIDE.X[i], DECIDE.Y[i]), (DECIDE.X[i+1], DECIDE.Y[i+1]), (DECIDE.X[i+2], DECIDE.Y[i+2])
        if p2 == p1 or p2 == p3: continue # angle is undefined
        
        angle = angle_between_vectors(p2-p1, p2-p3)
        if angle < DECIDE.PI - DECIDE.PARAMETERS.EPSILON or angle > DECIDE.PI + DECIDE.PARAMETERS.EPSILON:
            return True
    
    return False # no such set of points exists