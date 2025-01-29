import math

def distance(px1, py1, px2, py2) -> bool:
    return math.sqrt(math.pow(px1 - px2, 2) + math.pow(py1 - py2, 2))


def lic_0(X, Y, LENGTH1) -> bool:
    for i in range(len(X) - 1):
        if distance(X[i], Y[i], X[i+1], Y[i+1]) > LENGTH1:
            return True
        
    return False # no such set of points exists


def lic_1(X, Y, RADIUS1) -> bool:
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
    
    for i in range(len(X) - 2):
        R = circumcircle_radius(X[i], Y[i], X[i+1], Y[i+1], X[i+2], Y[i+2])
        if R > RADIUS1:
            return True
    return False # no such set of points exists


def lic_2(X, Y, EPSILON, PI = 3.1415926535):
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
    
    for i in range(len(X) - 2):
        p1, p2, p3 = (X[i], Y[i]), (X[i+1], Y[i+1]), (X[i+2], Y[i+2])
        if p2 == p1 or p2 == p3: continue # angle is undefined
        
        angle = angle_between_vectors(p2-p1, p2-p3)
        if angle < PI - EPSILON or angle > PI + EPSILON:
            return True
    
    return False # no such set of points exists


def lic_3(X, Y, AREA1):
    def triangle_area(point1, point2, point3):
        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = point3

        # Using the determinant formula for the area of a triangle
        area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
        return area
    
    for i in range(len(X) - 2):      
        p1, p2, p3 = (X[i], Y[i]), (X[i+1], Y[i+1]), (X[i+2], Y[i+2])
        if p2 == p1 or p2 == p3: continue # angle is undefined

        area = triangle_area(p1, p2, p3)
        if area > AREA1:
            return True
    
    return False # no such set of points exists