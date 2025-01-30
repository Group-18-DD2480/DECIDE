import unittest
from src.decide import CONNECTORS, InvalidInputException
from src.PUM import PUM

class TestPUM(unittest.TestCase):
    def test_PUM_ok(self):
        CMV = [ True , False, True ]
        LCM = [[CONNECTORS.ANDD, CONNECTORS.NOTUSED, CONNECTORS.ORR ],
            [CONNECTORS.NOTUSED, CONNECTORS.ANDD, CONNECTORS.ANDD],
            [CONNECTORS.ORR, CONNECTORS.ANDD ,CONNECTORS.ANDD ]]
        expected_PUM = [[None, True, True],
            [None, None, False],
            [True, False, None]]
        
        result_PUM = PUM(CMV,LCM,3)
        
        self.assertEqual(expected_PUM, result_PUM)
        
    def test_PUM_wrong_sizes(self):
        CMV = [ True , False ]
        LCM = [[CONNECTORS.ANDD, CONNECTORS.NOTUSED, CONNECTORS.ORR ],
            [CONNECTORS.NOTUSED, CONNECTORS.ANDD, CONNECTORS.ANDD],
            [CONNECTORS.ORR, CONNECTORS.ANDD ,CONNECTORS.ANDD ]]
        
        self.assertRaises(InvalidInputException, PUM, CMV, LCM, 3)
        
    def test_PUM_not_simmetric(self):
        CMV = [ True , False, True ]
        LCM = [[CONNECTORS.ANDD, CONNECTORS.NOTUSED, CONNECTORS.ORR ],
            [CONNECTORS.NOTUSED, CONNECTORS.ANDD, CONNECTORS.ANDD],
            [CONNECTORS.ANDD, CONNECTORS.ORR ,CONNECTORS.ANDD ]]
        
        self.assertRaises(InvalidInputException, PUM, CMV, LCM, 3)
        
