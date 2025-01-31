import PUM, FUV, LAUNCH, CMV
from utils import CONNECTORS, InvalidInputException

# PARAMETERS T
class PARAMETERS_T:
    def __init__(self):
        self.LENGTH1 = 2.0  # Length in LICs 0, 7, 12
        self.RADIUS1 = 3.0  # Radius in LICs 1, 8, 13
        self.EPSILON = 0.05  # Deviation from PI in LICs 2, 9
        self.AREA1 = 10.0  # Area in LICs 3, 10, 14
        self.QPTS = 3  # No. of consecutive points in LIC 4
        self.QUADS = 2  # No. of quadrants in LIC 4
        self.DIST = 1.5  # Distance in LIC 6
        self.NPTS = 3  # No. of consecutive pts. in LIC 6
        self.KPTS = 1  # No. of int. pts. in LICs 7, 12
        self.APTS = 1  # No. of int. pts. in LICs 8, 13
        self.BPTS = 1  # No. of int. pts. in LICs 8, 13
        self.CPTS = 1  # No. of int. pts. in LIC 9
        self.DPTS = 2  # No. of int. pts. in LIC 9
        self.EPTS = 1  # No. of int. pts. in LICs 10, 14
        self.FPTS = 1  # No. of int. pts. in LICs 10, 14
        self.GPTS = 1  # No. of int. pts. in LIC 11
        self.LENGTH2 = 5.0  # Maximum length in LIC 12
        self.RADIUS2 = 6.0  # Maximum radius in LIC 13
        self.AREA2 = 20.0  # Maximum area in LIC 14

# Global variable declarations
PARAMETERS = PARAMETERS_T()

# X coordinates of data points
X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Y coordinates of data points
Y = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Number of data points
NUMPOINTS = 10

# Logical Connector Matrix
LCM = [[ CONNECTORS.NOTUSED for _ in range(15)] for _ in range(15)] # 2D array of CONNECTORS
for i in range(15):
    for j in range(15):
        if i == j:
            LCM[i][j] = CONNECTORS.ANDD
        elif (i + j) % 3 == 0:
            LCM[i][j] = CONNECTORS.ORR

# Preliminary Unlocking Matrix
PUM_value = []  # 2D array of booleans

#  Preliminary Unlocking Vector.
PUV = [True if i % 2 == 0 else False for i in range(15)] # Array of booleans

# Conditions Met Vector
CMV_values = []  # Array of booleans

# Final Unlocking Vector
FUV_value = []  # Array of booleans

# Decision: Launch or No Launch
LAUNCH_value = False

def validate_inputs():
    """
    Validates global input variables. Raises InvalidInputException if any are invalid.
    """
    if not (2 <= NUMPOINTS <= 100):
        raise InvalidInputException("NUMPOINTS must be between 2 and 100.")
    
    if len(X) != NUMPOINTS or len(Y) != NUMPOINTS:
        raise InvalidInputException("X and Y must have exactly NUMPOINTS elements.")
    
    if not (len(LCM) == 15 and all(len(row) == 15 for row in LCM)):
        raise InvalidInputException("LCM must be a 15x15 matrix.")
    
    if len(PUV) != 15:
        raise InvalidInputException("PUV must be a list of 15 boolean values.")
    
    for param in [PARAMETERS.LENGTH1, PARAMETERS.RADIUS1, PARAMETERS.EPSILON, PARAMETERS.AREA1, 
                  PARAMETERS.DIST, PARAMETERS.LENGTH2, PARAMETERS.RADIUS2, PARAMETERS.AREA2]:
        if param < 0:
            raise InvalidInputException("All distance, radius, epsilon, and area parameters must be non-negative.")
    
    if not (2 <= PARAMETERS.QPTS <= NUMPOINTS):
        raise InvalidInputException("QPTS must be between 2 and NUMPOINTS.")
    
    if not (1 <= PARAMETERS.QUADS <= 3):
        raise InvalidInputException("QUADS must be between 1 and 3.")
    
    for param in [PARAMETERS.NPTS, PARAMETERS.KPTS, PARAMETERS.APTS, PARAMETERS.BPTS, 
                  PARAMETERS.CPTS, PARAMETERS.DPTS, PARAMETERS.EPTS, PARAMETERS.FPTS, PARAMETERS.GPTS]:
        if param < 1 or param > NUMPOINTS - 2:
            raise InvalidInputException(f"{param} must be between 1 and NUMPOINTS-2.")


def DECIDE():
    """
    Determines the final launch decision based on the given input data.

    This function processes global variables and computes intermediate results to decide 
    whether a launch should proceed. The decision is printed as "YES" or "NO".

    Global Variables Used:
        NUMPOINTS (int): The number of planar data points.
        X and Y: Arrays containing the coordinates of data points.
        PARAMETERS: Holds parameters for LICs (Launch Interceptor Conditions).
        LCM (list of list of connectors): Logical Connector Matrix defining conditions between LICs.
        PUV (list of bool): Preliminary Unlocking Vector controlling PUM evaluation.

    Intermediate Results:
        CMV (list of bool): Conditions Met Vector indicating which LICs are met.
        PUM (list of list of bool): Preliminary Unlocking Matrix, computed using LCM and CMV.
        FUV (list of bool): Final Unlocking Vector derived from PUM and PUV.

    Output:
        Prints the final launch decision ("YES" or "NO") to standard output.
    """
    
    validate_inputs()
    
    CMV_values = [
        CMV.lic_0(X, Y, PARAMETERS.LENGTH1),
        CMV.lic_1(X, Y, PARAMETERS.RADIUS1),
        CMV.lic_2(X, Y, PARAMETERS.EPSILON),
        CMV.lic_3(X, Y, PARAMETERS.AREA1),
        CMV.lic_4(X, Y, PARAMETERS.QPTS, PARAMETERS.QUADS),
        CMV.lic_5(X, Y),
        CMV.lic_6(X, Y, PARAMETERS.NPTS, PARAMETERS.DIST),
        CMV.lic_7(X, Y, PARAMETERS.KPTS, PARAMETERS.LENGTH1),
        CMV.lic_8(X, Y, PARAMETERS.APTS, PARAMETERS.BPTS, PARAMETERS.RADIUS1),
        CMV.lic_9(X, Y, PARAMETERS.CPTS, PARAMETERS.DPTS, PARAMETERS.EPSILON),
        CMV.lic_10(X, Y, PARAMETERS.EPTS, PARAMETERS.FPTS, PARAMETERS.AREA1),
        CMV.lic_11(X, PARAMETERS.GPTS),
        CMV.lic_12(X, Y, PARAMETERS.KPTS, PARAMETERS.LENGTH1, PARAMETERS.LENGTH2),
        CMV.lic_13(X, Y, PARAMETERS.APTS, PARAMETERS.BPTS, PARAMETERS.RADIUS1, PARAMETERS.RADIUS2),
        CMV.lic_14(X, Y, PARAMETERS.EPTS, PARAMETERS.FPTS, PARAMETERS.AREA1, PARAMETERS.AREA2),
    ]
    
    PUM_value = PUM.PUM(LCM, CMV_values)
    
    FUV_value = FUV.FUV(PUM_value,PUV)
    
    LAUNCH_value = LAUNCH.LAUNCH(FUV_value) 
    
    print("LAUNCH decision: ", "YES" if LAUNCH_value else "NO")
    print("\n")
    
    print("CMV (Conditions Met Vector): ")
    print(CMV_values)
    print("\n")
    
    print("PUM (Preliminary Unlocking Matrix): ")
    for row in PUM_value:
        print(row)
    print("\n")
    
    print("FUV (Final Unlocking Vector): ")
    print(FUV_value)
    print("\n")
    
    pass

if __name__ == "__main__":
    DECIDE()

