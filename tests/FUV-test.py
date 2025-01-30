import unittest


rows, cols = 15, 15  
def FUV(PUM, PUV):
    return [False for _ in range(rows)]
class TestFUV(unittest.TestCase):
    
    def PUV_all_false(self):
        PUM = [[False] * cols for _ in range(rows)]
        PUV = [False for _ in range(rows)]
        FUV = FUV(PUM, PUV)
        for i in range(rows):
            self.assertTrue(FUV[i])
    def PUV_and_PUM_all_true(self):
        PUM = [[True] * cols for _ in range(rows)]
        PUV = [True for _ in range(rows)]
        FUV = FUV(PUM, PUV)
        for i in range(rows):
            self.assertTrue(FUV[i])
    
    def PUM_all_false(self):
        PUM = [[False] * cols for _ in range(rows)]
        PUV = [True for _ in range(rows)]
        FUV = FUV(PUM, PUV)
        for i in range(rows):
            self.assertFalse(FUV[i])
    def PUM_one_false_in_every_row(self):
        PUM = [[True] * cols for _ in range(rows)]
        PUV = [True for _ in range(rows)]
        for i in range(rows):
            PUM[i][i] = False
        FUV = FUV(PUM, PUV)
        for i in range(rows):
            self.assertFalse(FUV[i])
    def general_PUM_and_PUV(self):
        PUM = [
            [False, True, True, True, True, True, True, True, False, False, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, False, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, False, False, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, False, True, False, True, True, True, False],
            [True, True, True, True, False, True, True, True, False, False, False, True, True, True, True],
            
            [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, False, True, True, True, True, True, True, False, False, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, False, False, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, False, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, False, True, False, True, True, True, True],
            
            [True, True, True, True, True, True, True, True, False, False, False, True, True, True, True],
            [True, True, True, True, True, False, True, True, False, False, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, False, False, False, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
        ]
        PUV = [False, True, False, True, True, 
               True, True, True, False, False, 
               True, True, False, True, True]
        FUV_func = FUV(PUM,PUV)
        FUV_test = [True, False, True, False, False, 
                    True, False, False, True, True,
                    False, False, True, True, True]
        self.assertEqual(FUV_func, FUV_test)