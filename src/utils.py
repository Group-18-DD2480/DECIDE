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
        
class InvalidInputException(Exception):
    """Custom exception for invalid input."""
    def __init__(self, message="Invalid input provided"):
        self.message = message
        super().__init__(self.message)
