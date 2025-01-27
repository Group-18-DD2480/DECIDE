import math

EPSILON = 1e-7  # Small tolerance for floating point comparisons

def calculate_distance(x1, y1, x2, y2):
    """Calculate the distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
def lic_4(X, Y, Q_PTS, QUADS) -> bool:
    def quadrant(px, py)->int:
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
        nbr_quads = [0,0,0,0]
        for j in range(Q_PTS):
            nbr_quads[quad[i+j]] = 1
        if (QUADS < nbr_quads.count(1)):
            return True
    return False

def lic_5(X,Y)-> bool:
    if len(X) < 2:
        return False
    for i in range(len(X)-1):
        if (X[i+1] - X[i] < 0):
            return True
    return False

def lic_6(X,Y, N_PTS, DIST)->bool:
    if len(X) < 3 or len(X) < N_PTS:
        return False
    for i in range(len(X) - N_PTS + 1):
        end = i+N_PTS-1
        if (X[i] == X[end] and Y[i] == Y[end]):
            #disregard first and last points
            for j in range(1,N_PTS-1):
                if DIST < calculate_distance(X[i],Y[i],X[i+j],Y[i+j]):
                    return True
        else:
            for j in range(1,N_PTS-1):
                dist = abs((Y[i]-Y[end])*X[i+j] - (X[i]-X[end])*Y[i+j] + X[i]*Y[end] - X[end]*Y[i]) / calculate_distance(X[i], Y[i], X[end], Y[end])
                if DIST < dist:
                    return True
    return False

def lic_10(X, Y, E_PTS, F_PTS, AREA1):
    if (n := len(X)) < 5:
        return False
    for a in range(n):
        b = a + E_PTS + 1
        c = b + F_PTS + 1
        if c < n:
            if (abs(X[a]*(Y[b] - Y[c]) + X[b]*(Y[c] - Y[a]) + X[c]*(Y[a] - Y[b])) / 2.0) > AREA1:
                print((abs(X[a]*(Y[b] - Y[c]) + X[b]*(Y[c] - Y[a]) + X[c]*(Y[a] - Y[b])) / 2.0))
                return True
    return False


def lic_11(X, G_PTS):
    if (n := len(X)) < 3:
        return False
    for a in range(n):
        b = a + G_PTS + 1
        if b < n and (X[b] - X[a]) < 0:
            return True
    return False


def lic_12(X, Y, K_PTS, LENGTH1, LENGTH2):
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

def calculate_distance(x1, y1, x2, y2):
    """Calculate the distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
def calculate_area(x1, y1, x2, y2, x3, y3):
    """Calculate the area of a triangle given three points (x1, y1), (x2, y2), (x3, y3)."""
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

def lic_13(X, Y, A_PTS, B_PTS, RADIUS1, RADIUS2):
    """
    Determine if LIC 13 is met.

    Parameters:
    - X: List of X coordinates.
    - Y: List of Y coordinates.
    - A_PTS: Number of intervening points between the first and second points.
    - B_PTS: Number of intervening points between the second and third points.
    - RADIUS1: Radius for the first circle condition.
    - RADIUS2: Radius for the second circle condition.

    Returns:
    - Boolean indicating if LIC 13 is met.
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
    Determine if LIC 14 is met.

    Parameters:
    - X: List of X coordinates.
    - Y: List of Y coordinates.
    - E_PTS: Number of intervening points between the first and second points.
    - F_PTS: Number of intervening points between the second and third points.
    - AREA1: Area for the first triangle condition.
    - AREA2: Area for the second triangle condition.

    Returns:
    - Boolean indicating if LIC 14 is met.
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


import math
