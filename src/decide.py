from CMV import *
# CONSTANT
PI = 3.1415926535

# TYPE DECLARATIONS
class CONNECTORS:
    def NOTUSED(i = None, j = None):
        return True
    
    def ANDD(i,j):
        return i and j

    def ORR(i,j):
        return i or j

class COMPTYPE:
    LT = 1111
    EQ = 1112
    GT = 1113

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
PUM = []  # 2D array of booleans

# Conditions Met Vector
CMV = []  # Array of booleans

# Final Unlocking Vector
FUV = []  # Array of booleans

# Decision: Launch or No Launch
LAUNCH = False

class InvalidInputException(Exception):
    """Custom exception for invalid input."""
    def __init__(self, message="Invalid input provided"):
        self.message = message
        super().__init__(self.message)

def DECIDE():
    CMV = [
        lic_0(X, Y, PARAMETERS_T.LENGTH1),
        lic_1(X, Y, PARAMETERS_T.RADIUS1),
        lic_2(X, Y, PARAMETERS_T.EPSILON),
        lic_3(X, Y, PARAMETERS_T.AREA1),
        lic_4(X, Y, PARAMETERS_T.Q_PTS, PARAMETERS_T.QUADS),
        lic_5(X, Y),
        lic_6(X, Y, PARAMETERS_T.N_PTS, PARAMETERS_T.DIST),
        lic_7(X, Y, PARAMETERS_T.K_PTS, PARAMETERS_T.LENGHT1),
        lic_8(X, Y, PARAMETERS_T.A_PTS, PARAMETERS_T.B_PTS, PARAMETERS_T.RAIDUS1),
        lic_9(X, Y, PARAMETERS_T.C_PTS, PARAMETERS_T.D_PTS, PARAMETERS_T.EPSILON),
        lic_10(X, Y, PARAMETERS_T.E_PTS, PARAMETERS_T.F_PTS, PARAMETERS_T.AREA1),
        lic_11(X, PARAMETERS_T.G_PTS),
        lic_12(X, Y, PARAMETERS_T.K_PTS, PARAMETERS_T.LENGTH1, PARAMETERS_T.LENGTH2),
        lic_13(X, Y, PARAMETERS_T.A_PTS, PARAMETERS_T.B_PTS, PARAMETERS_T.RADIUS1, PARAMETERS_T.RADIUS2),
        lic_14(X, Y, PARAMETERS_T.E_PTS, PARAMETERS_T.F_PTS, PARAMETERS_T.AREA1, PARAMETERS_T.AREA2),
    ]
    
    #TODO: continue after impl of PUM and FUV
    
    pass
