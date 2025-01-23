# CONSTANT
PI = 3.1415926535

# TYPE DECLARATIONS
class CONNECTORS:
    def NOTUSED(pair = None):
        return None
    
    def ANDD(pair):
        return pair[0] and pair[1]

    def ORR(pair):
        return pair[0] or pair[1]

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
PARAMETERS2 = PARAMETERS_T()

# X coordinates of data points
X = []
X2 = []

# Y coordinates of data points
Y = []
Y2 = []

# Number of data points
NUMPOINTS = 0
NUMPOINTS2 = 0

# Logical Connector Matrix
LCM = []  # 2D array of CONNECTORS
LCM2 = []

# Preliminary Unlocking Matrix
PUM = []  # 2D array of booleans
PUM2 = []

# Conditions Met Vector
CMV = []  # Array of booleans
CMV2 = []

# Final Unlocking Vector
FUV = []  # Array of booleans
FUV2 = []

# Decision: Launch or No Launch
LAUNCH = False
LAUNCH2 = False

def DOUBLECOMPARE(A, B):
    """Compares floating point numbers."""
    if abs(A - B) < 0.00001:
        return COMPTYPE.EQ
    if A < B:
        return COMPTYPE.LT
    return COMPTYPE.GT

def DECIDE():
    """Function we must write."""
    pass
