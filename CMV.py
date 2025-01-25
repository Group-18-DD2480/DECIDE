import decide as DECIDE
import math

def distance(px1, py1, px2, py2) -> bool:
    return math.sqrt(math.pow(px1 - px2, 2) + math.pow(py1 - py2, 2))


def lic_0() -> bool:
    for i in range(DECIDE.NUMPOINTS - 1):
        if distance(DECIDE.X[i], DECIDE.Y[i], DECIDE.X[i+1], DECIDE.Y[i+1]) > DECIDE.PARAMETERS.LENGTH1:
            return True
        
    return False # no such set of points exists