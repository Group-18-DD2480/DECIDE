import math


def calculate_distance(x1, y1, x2, y2):
    """Calculate the distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def lic_4(X, Y, Q_PTS, QUADS) -> bool:
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
    if len(X) < 2:
        return False
    for i in range(len(X) - 1):
        if X[i + 1] - X[i] < 0:
            return True
    return False


def lic_6(X, Y, N_PTS, DIST) -> bool:
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
    """Check if there are two points separated by K_PTS points with distance > LENGTH1"""
    if len(X) < 3:
        return False

    for i in range(len(X) - K_PTS - 1):
        dist = calculate_distance(X[i], Y[i], X[i + K_PTS + 1], Y[i + K_PTS + 1])
        if dist > LENGTH1:
            return True
    return False


def lic_8(X, Y, A_PTS, B_PTS, RADIUS1) -> bool:
    """Check if any three points separated by A_PTS and B_PTS cannot be contained in a circle"""
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
    """Check if three points separated by C_PTS and D_PTS form an angle outside [PI±EPSILON]"""
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


def lic_10(X, Y, E_PTS, F_PTS, AREA1):
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
