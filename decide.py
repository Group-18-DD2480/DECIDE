from src import PUM, FUV, LAUNCH, CMV

# PARAMETERS T
class PARAMETERS_T:
    def __init__(self):
        self.LENGTH1 = 0.0  # Length in LICs 0, 7, 12
        self.RADIUS1 = 0.0  # Radius in LICs 1, 8, 13
        self.EPSILON = 0.0  # Deviation from PI in LICs 2, 9
        self.AREA1 = 0.0  # Area in LICs 3, 10, 14
        self.QPTS = 0  # No. of consecutive points in LIC 4
        self.QUADS = 0  # No. of quadrants in LIC 4
        self.DIST = 0.0  # Distance in LIC 6
        self.NPTS = 0  # No. of consecutive pts. in LIC 6
        self.KPTS = 0  # No. of int. pts. in LICs 7, 12
        self.APTS = 0  # No. of int. pts. in LICs 8, 13
        self.BPTS = 0  # No. of int. pts. in LICs 8, 13
        self.CPTS = 0  # No. of int. pts. in LIC 9
        self.DPTS = 0  # No. of int. pts. in LIC 9
        self.EPTS = 0  # No. of int. pts. in LICs 10, 14
        self.FPTS = 0  # No. of int. pts. in LICs 10, 14
        self.GPTS = 0  # No. of int. pts. in LIC 11
        self.LENGTH2 = 0.0  # Maximum length in LIC 12
        self.RADIUS2 = 0.0  # Maximum radius in LIC 13
        self.AREA2 = 0.0  # Maximum area in LIC 14

# Global variable declarations
PARAMETERS = PARAMETERS_T()

# X coordinates of data points
X = []

# Y coordinates of data points
Y = []

# Number of data points
NUMPOINTS = 0

# Logical Connector Matrix
LCM = []  # 2D array of CONNECTORS

# Preliminary Unlocking Matrix
PUM_value = []  # 2D array of booleans

#  Preliminary Unlocking Vector.
PUV = [] # Array of booleans

# Conditions Met Vector
CMV_values = []  # Array of booleans

# Final Unlocking Vector
FUV_value = []  # Array of booleans

# Decision: Launch or No Launch
LAUNCH_value = False

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
    
    #TODO wait for launch function impl then call it and print
    
    print("CMV (Conditions Met Vector): ")
    print(CMV)
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

