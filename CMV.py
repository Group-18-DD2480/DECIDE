import math

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
            
        if dist > RADIUS1:
            subcond1 = True

        if dist <= RADIUS2:
            subcond2 = True

        # when both subconditions are ok, exit and return True
        if subcond1 and subcond2:
            return True

    
    return subcond1 and subcond2