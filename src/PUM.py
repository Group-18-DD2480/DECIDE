from src.decide import InvalidInputException

def PUM(LCM, CMV):
    
    if not isinstance(LCM, list) or not isinstance(CMV, list):
        raise InvalidInputException
    
    LENGTH = len(CMV)
    
    if len(LCM) != LENGTH or any(len(row) != LENGTH for row in LCM):
        raise InvalidInputException
    
    PUM = []
    for i in range(LENGTH):
        tempRow = []
        
        for j in range(LENGTH):
            
            if i == j :
                tempRow.append(None)
            elif LCM[i][j] == LCM[j][i] :
                tempRow.append(LCM[i][j](CMV[i], CMV[j]))
            else:
                raise InvalidInputException
            
        PUM.append(tempRow)
    return PUM
