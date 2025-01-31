import unittest
from src.PUM import PUM
from src.utils import CONNECTORS, InvalidInputException

class TestPUM(unittest.TestCase):
    """Test suite for PUM.
    
    calculate the logical operation in LCM[i][j] wih values CMV[i],CMV[j].
    NOTUSED means that it should be set to True regardless.
    """
    def test_PUM_ok(self):
        """ Test valid operations, such as False and True, Notused, and or """
        CMV = [ True , False, True ]
        LCM = [[CONNECTORS.ANDD, CONNECTORS.NOTUSED, CONNECTORS.ORR ],
            [CONNECTORS.NOTUSED, CONNECTORS.ANDD, CONNECTORS.ANDD],
            [CONNECTORS.ORR, CONNECTORS.ANDD ,CONNECTORS.ANDD ]]
        expected_PUM = [[None, True, True],
            [True, None, False],
            [True, False, None]]
        
        result_PUM = PUM(LCM,CMV)
        
        self.assertEqual(expected_PUM, result_PUM)
        
    def test_PUM_wrong_sizes(self):
        """test that PUM fails when the sizes are not compatible"""
        CMV = [ True , False ]
        LCM = [[CONNECTORS.ANDD, CONNECTORS.NOTUSED, CONNECTORS.ORR ],
            [CONNECTORS.NOTUSED, CONNECTORS.ANDD, CONNECTORS.ANDD],
            [CONNECTORS.ORR, CONNECTORS.ANDD ,CONNECTORS.ANDD ]]
        
        self.assertRaises(InvalidInputException, PUM, LCM, CMV)
        
    def test_PUM_not_simmetric(self):
        """test that PUM fails when LCM is not simmetric as it shoud"""
        CMV = [ True , False, True ]
        LCM = [[CONNECTORS.ANDD, CONNECTORS.NOTUSED, CONNECTORS.ORR ],
            [CONNECTORS.NOTUSED, CONNECTORS.ANDD, CONNECTORS.ANDD],
            [CONNECTORS.ANDD, CONNECTORS.ORR ,CONNECTORS.ANDD ]]
        
        self.assertRaises(InvalidInputException, PUM, LCM, CMV)
        
