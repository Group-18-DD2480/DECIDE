import math


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