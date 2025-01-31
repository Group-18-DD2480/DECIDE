from utils import InvalidInputException

def PUM(LCM, CMV):
    """
    Constructs the Preliminary Unlocking Matrix (PUM) based on the Logical Connector Matrix (LCM) and the Conditions Met Vector (CMV).

    Args:
        LCM (list of list of callable or None): A symmetric square matrix where each element is a function (e.g., `lambda x, y: x and y`) 
            representing a logical operation to be applied to corresponding elements of CMV.
        CMV (list of bool): A vector containing boolean values that indicate conditions met.

    Returns:
        list of list: A square matrix PUM where each entry PUM[i][j] is determined by applying LCM[i][j] to CMV[i] and CMV[j].
        The diagonal entries are set to `None`.

    Raises:
        InvalidInputException: If LCM or CMV is not a list, if their sizes do not match, or if LCM 
            is not symmetric.
    """
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
