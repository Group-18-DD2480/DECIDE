import math
EPSILON = 1e-7  # Small tolerance for floating point comparisons

def calculate_distance(x1, y1, x2, y2):
    """Calculate the distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_area(x1, y1, x2, y2, x3, y3):
    """Calculate the area of a triangle given three points (x1, y1), (x2, y2), (x3, y3)."""
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

def lic_0(X, Y, LENGTH1) -> bool:
    """Checks if there exists two consecutive points further apart than LENGTH1
    \nParameters:
    - X: List of X coordinates
    - Y: List of Y coordinates
    - LENGTH1: Float
    \nReturns:
    - Boolean indicating if the set exists.
    """
    for i in range(len(X) - 1):
        if calculate_distance(X[i], Y[i], X[i+1], Y[i+1]) > LENGTH1:
            return True
        
    return False # no such set of points exists


def lic_1(X, Y, RADIUS1) -> bool:
    """Checks if there exists a set of 3 consecutive points that cannot be contained in a circle of radius RADIUS1
    \nParameters:
    - X: List of X coordinates
    - Y: List of Y coordinates
    - RADIUS1: Float for radius
    \nReturns:
    - Boolean indicating if the set exists.
    """
    def circumcircle_radius(px1, py1, px2, py2, px3, py3):
        # Calculate pairwise distances
        a = calculate_distance(px1, py1, px2, py2)
        b = calculate_distance(px1, py1, px3, py3)
        c = calculate_distance(px2, py2, px3, py3)

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


def lic_2(X, Y, EPSILON, PI = 3.1415926535) -> bool:
    """Checks is there exists a set of three consecutive points that form an angle smaller than PI-EPSILON or larger than PI+EPSILON
    with the second point being the vertex of the angle
    \nParameters:
    - X: List of X coordinates
    - Y: List of Y coordinates
    - EPSILON: Angle in radians
    - PI: optional value for PI, defaults to value of pi
    \nReturns:
    - Boolean indicating if the set exists.
    """
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
        
        angle = angle_between_vectors((p2[0] - p1[0], p2[1] - p1[1]), (p2[0] - p3[0], p2[1] - p3[1]))
        if angle < PI - EPSILON or angle > PI + EPSILON:
            return True
    
    return False # no such set of points exists


def lic_3(X, Y, AREA1) -> bool:
    """Checks the existence of a set of three consecutive points that form a triangle with an area greater than AREA1
    \nParameters:
    - X: List of X coordinates
    - Y: List of Y coordinates
    - AREA1: Float for area
    \nReturns:
    - Boolean indicating if the set exists.
    """
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

def lic_4(X, Y, Q_PTS, QUADS) -> bool:
    """Checks for the existence of a set of Q_PTS consecutive points such that they lie within more than QUADS quadrants.
    In the case of points on borders, priority should be given to the smallest quadrant number, which start at 1 in the (+,+) quadrant and go counter-clockwise
    \nParameters:
    - X: List of X coordinates
    - Y: List of Y coordinates
    - Q_PTS: Number of points to consider
    - QUADS: Number of quadrants (0 <= QUADS <= 3)
    \nReturns:
    - Boolean indicating if the set exists.
    """
    
    def quadrant(px, py) -> int:
        if px >= 0 and py >= 0:
            return 0
        elif px < 0 and py >= 0:
            return 1
        elif px <= 0 and py < 0:
            return 2
        else:
            return 3

    if len(X) < Q_PTS:
        return False

    quad = []
    for i in range(len(X)):
        quad.append(quadrant(X[i], Y[i]))
    for i in range(len(X) - Q_PTS + 1):
        nbr_quads = [0, 0, 0, 0]
        for j in range(Q_PTS):
            nbr_quads[quad[i + j]] = 1
        if QUADS < nbr_quads.count(1):
            return True
    return False


def lic_5(X, Y) -> bool:
    """Checks for two consecutive points where the second point's x coordinate is smaller than the first's
    \nParameters:
    - X: List of X coordinates
    - Y: List of Y coordinates
    \nReturns:
    - Boolean indicating if the set exists.
    """
    
    if len(X) < 2:
        return False
    for i in range(len(X) - 1):
        if X[i + 1] - X[i] < 0:
            return True
    return False


def lic_6(X, Y, N_PTS, DIST) -> bool:
    """Checks the existence of a set of N_PTS consecutive points such that at least one point is at a distance greater than DIST from the line that joins the first and last points.
    \nParameters:
    - X: List of X coordinates
    - Y: List of Y coordinates
    - N_PTS: Number of points to consider (3 <= N_PTS )
    - DIST: Float for distance (0 <= DIST)
    \nReturns:
    - Boolean indicating if the set exists.
    """
    if len(X) < 3 or len(X) < N_PTS:
        return False
    for i in range(len(X) - N_PTS + 1):
        end = i + N_PTS - 1
        if X[i] == X[end] and Y[i] == Y[end]:
            # disregard first and last points
            for j in range(1, N_PTS - 1):
                if DIST < calculate_distance(X[i], Y[i], X[i + j], Y[i + j]):
                    return True
        else:
            for j in range(1, N_PTS - 1):
                dist = abs(
                    (Y[i] - Y[end]) * X[i + j]
                    - (X[i] - X[end]) * Y[i + j]
                    + X[i] * Y[end]
                    - X[end] * Y[i]
                ) / calculate_distance(X[i], Y[i], X[end], Y[end])
                if DIST < dist:
                    return True
    return False


def lic_7(X, Y, K_PTS, LENGTH1) -> bool:
    """Check if there are two points separated by K_PTS points with distance > LENGTH1
    \nParameters
    - X: List of X coordinates
    - Y: List of Y coordinates
    - K_PTS: Number of points to consider (1 <= K_PTS )
    - LENGTH1: Float for distance
    \nReturns:
    - Boolean indicating if the set exists.
    """
    if len(X) < 3:
        return False

    for i in range(len(X) - K_PTS - 1):
        dist = calculate_distance(X[i], Y[i], X[i + K_PTS + 1], Y[i + K_PTS + 1])
        if dist > LENGTH1:
            return True
    return False


def lic_8(X, Y, A_PTS, B_PTS, RADIUS1) -> bool:
    """Check if any three points separated by A_PTS and B_PTS cannot be contained in a circle
    \nParameters
    - X: List of X coordinates
    - Y: List of Y coordinates
    - A_PTS: Number of points between first and second point (1 <= A_PTS )
    - B_PTS: Number of points between second and third point (1 <= B_PTS )
    - RADIUS1: Float for radius
    \nReturns:
    - Boolean indicating if the set exists.
    """
    if len(X) < 5:
        return False

    for i in range(len(X) - A_PTS - B_PTS - 2):
        x1, y1 = X[i], Y[i]
        x2, y2 = X[i + A_PTS + 1], Y[i + A_PTS + 1]
        x3, y3 = X[i + A_PTS + B_PTS + 2], Y[i + A_PTS + B_PTS + 2]

        # Calculate distances between points
        a = calculate_distance(x1, y1, x2, y2)
        b = calculate_distance(x2, y2, x3, y3)
        c = calculate_distance(x3, y3, x1, y1)

        # If points form a line, check if distance between furthest points > 2*RADIUS1
        if (a + b == c) or (b + c == a) or (a + c == b):
            if max(a, b, c) > 2 * RADIUS1:
                return True
            continue

        # Calculate radius of circumscribed circle
        s = (a + b + c) / 2  # Semi-perimeter
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        radius = (a * b * c) / (4 * area)

        if radius > RADIUS1:
            return True
    return False


def lic_9(X, Y, C_PTS, D_PTS, EPSILON) -> bool:
    """Check if there exists three points separated by C_PTS and D_PTS form an angle outside [PI±EPSILON]
    \nParameters
    - X: List of X coordinates
    - Y: List of Y coordinates
    - C_PTS: Number of points between first and second point (1 <= C_PTS )
    - D_PTS: Number of points between second and third point (1 <= D_PTS )
    - EPSILON: Angle in radians
    \nReturns:
    - Boolean indicating if the set exists.
    """
    if len(X) < 5:
        return False

    for i in range(len(X) - C_PTS - D_PTS - 2):
        x1, y1 = X[i], Y[i]
        x2, y2 = X[i + C_PTS + 1], Y[i + C_PTS + 1]  # Vertex
        x3, y3 = X[i + C_PTS + D_PTS + 2], Y[i + C_PTS + D_PTS + 2]

        # Skip if points coincide with vertex
        if (x1 == x2 and y1 == y2) or (x3 == x2 and y3 == y2):
            continue

        # Calculate vectors
        v1x, v1y = x1 - x2, y1 - y2
        v2x, v2y = x3 - x2, y3 - y2

        # Calculate dot product and magnitudes
        dot_product = v1x * v2x + v1y * v2y
        mag1 = math.sqrt(v1x * v1x + v1y * v1y)
        mag2 = math.sqrt(v2x * v2x + v2y * v2y)

        # Calculate angle
        cos_angle = dot_product / (mag1 * mag2)
        # Handle floating point errors
        if cos_angle > 1:
            cos_angle = 1
        elif cos_angle < -1:
            cos_angle = -1
        angle = math.acos(cos_angle)

        if angle < (math.pi - EPSILON) or angle > (math.pi + EPSILON):
            return True
    return False


def lic_10(X, Y, E_PTS, F_PTS, AREA1) -> bool:
    """Check if there exists three points separated by E_PTS and F_PTS form a triangle of area greater than AREA1
    \nParameters:
    - X: List of X coordinates
    - Y: List of Y coordinates
    - E_PTS: Number of points between first and second point (1 <= E_PTS )
    - F_PTS: Number of points between second and third point (1 <= F_PTS )
    - AREA1: Float for the area
    \nReturns:
    - Boolean indicating if the set exists.
    """
    if (n := len(X)) < 5:
        return False
    for a in range(n):
        b = a + E_PTS + 1
        c = b + F_PTS + 1
        if c < n:
            if (
                abs(X[a] * (Y[b] - Y[c]) + X[b] * (Y[c] - Y[a]) + X[c] * (Y[a] - Y[b]))
                / 2.0
            ) > AREA1:
                print(
                    (
                        abs(
                            X[a] * (Y[b] - Y[c])
                            + X[b] * (Y[c] - Y[a])
                            + X[c] * (Y[a] - Y[b])
                        )
                        / 2.0
                    )
                )
                return True
    return False


def lic_11(X, G_PTS) -> bool:
    """Checks if there exists 2 points separated by G_PTS points such that the second point's x coordinate is smaller than the first's
    \nParameters:
    - X: List of X coordinates
    - G_PTS: Number of points between first and second point (1 <= G_PTS)
    \nReturns:
    - Boolean indicating if the set exists.
    """
    if (n := len(X)) < 3:
        return False
    for a in range(n):
        b = a + G_PTS + 1
        if b < n and (X[b] - X[a]) < 0:
            return True
    return False


def lic_12(X, Y, K_PTS, LENGTH1, LENGTH2) -> bool:
    """Checks if there exists two sets of two points both separated by K_PTS that are at 
    a distance greater than LENGTH1 for the first set and are a distance lesser than LENGTH2 for the second set.
    \nParameters:
    - X: List of X coordinates
    - Y: List of Y coordinates
    - K_PTS: Number of points between first and second point (1 <= K_PTS)
    - LENGTH1: Distance for first set
    - LENGTH2: Distance for second set
    \nReturns:
    - Boolean indicating if both sets exist.
    """
    if (n := len(X)) < 3:
        return False
    g, l = False, False
    for a in range(n):
        if (b := a + K_PTS + 1) < n:
            ab = math.sqrt(math.pow((X[b] - X[a]), 2) + math.pow((Y[b] - Y[a]), 2))
            g = g if g else ab > LENGTH1
            l = l if l else ab < LENGTH2
            if g and l:
                return True
    return False
def lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2):
    """
    Checks if there exists two sets of three points both separated by A_PTS and B_PTS 
    such that the first set of points cannot be contained within a circle of radius RADIUS1 
    and the second set of points can be contained within a circle of radius RADIUS2.
    \nParameters:
    - X: List of X coordinates.
    - Y: List of Y coordinates.
    - A_PTS: Number of intervening points between the first and second points.
    - B_PTS: Number of intervening points between the second and third points.
    - RADIUS1: Radius for the first circle condition.
    - RADIUS2: Radius for the second circle condition.
    \nReturns:
    - Boolean indicating if both sets exist.
    """

    subcond1 = False
    subcond2 = False

    if RADIUS1 < 0: 
        return False
    if RADIUS2 < 0: 
        return False
    if (n := len(X)) < 5:
        return False
    if A_PTS + B_PTS + 3 > n:
        return False

    for a in range(n):
        b = a + A_PTS + 1
        c = b + B_PTS + 1

        if(c>=n):
            break

        ab = calculate_distance(X[a], Y[a], X[b], Y[b])
        bc = calculate_distance(X[b], Y[b], X[c], Y[c])
        ca = calculate_distance(X[a], Y[a], X[c], Y[c])

        area = calculate_area(X[a], Y[a], X[b], Y[b], X[c], Y[c])

        if area == 0:  # Collinear points therefore use max dist to compare to raidus
            dist = max(ab,bc,ca)
        else:
            dist = (ab * bc * ca) / (4 * area) # Calculate the circumradius

        # Check if dist is greater than RADIUS1 with a tolerance
        if dist > RADIUS1 + EPSILON:
            subcond1 = True

        # Check if dist is less than or equal to RADIUS2 with a tolerance
        if dist <= RADIUS2 + EPSILON:
            subcond2 = True

        # When both subconditions are satisfied, return True
        if subcond1 and subcond2:
            return True

    return subcond1 and subcond2

def lic_14(X, Y, E_PTS, F_PTS, AREA1, AREA2):
    """
    Checks if there exists two sets of three points both separated by E_PTS and F_PTS 
    such that the first set of points form a triangle of area greater than AREA1 
    and the second set of points form a triangle of with area less than AREA2.
    \nParameters:
    - X: List of X coordinates.
    - Y: List of Y coordinates.
    - E_PTS: Number of intervening points between the first and second points.
    - F_PTS: Number of intervening points between the second and third points.
    - AREA1: Area for the first triangle condition.
    - AREA2: Area for the second triangle condition.
    \nReturns:
    - Boolean indicating if both sets exist.
    """
    subcond1 = False
    subcond2 = False

    if AREA1 < 0: 
        return False
    if AREA2 < 0: 
        return False
    if (n := len(X)) < 5:
        return False
    if E_PTS + F_PTS + 3 > n:
        return False

    for a in range(n):
        b = a + E_PTS + 1
        c = b + F_PTS + 1

        if(c>=n):
            break

        ab = calculate_distance(X[a], Y[a], X[b], Y[b])
        bc = calculate_distance(X[b], Y[b], X[c], Y[c])
        ca = calculate_distance(X[a], Y[a], X[c], Y[c])

        area = calculate_area(X[a], Y[a], X[b], Y[b], X[c], Y[c])

        # Check if area is greater than AREA1 with a tolerance
        if area > AREA1 + EPSILON:
            subcond1 = True

        # Check if area is less than AREA1 with a tolerance
        if area < AREA2 - EPSILON:
            subcond2 = True

        # When both subconditions are satisfied, return True
        if subcond1 and subcond2:
            return True

    return subcond1 and subcond2