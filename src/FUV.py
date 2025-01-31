from src.decide import InvalidInputException

def FUV(PUM, PUV):
    """
    Constructs the Final Unlocking Vector (FUV) based on the Preliminary Unlocking Matrix (PUM) and the Preliminary Unlocking Vector (CMV).

    Args:
        PUM (list of list of booleans): A symmetric square matrix where each element is a boolean or None.
        PUV (list of bool): A vector containing boolean values that whether the corresponding row in PUM should be considered or not.

    Returns:
        list: A square matrix PUM where each entry FUV[i] is set to True if PUV[i] is False or 
        if all PUM[i][j] are True disregarding PUM[i][i], otherwise it is False.
    
    Raises:
        InvalidInputException: If PUM or PUV is not a list, if their sizes do not match, if PUM 
            is not symmetric or if PUM doesn't have None one the diagonal.
    """
    if not isinstance(PUM, list) or not isinstance(PUV, list):
        raise InvalidInputException
    
    LENGTH = len(PUV)
    
    if len(PUM) != LENGTH or any(len(row) != LENGTH for row in PUM):
        raise InvalidInputException
    
    for i in range(LENGTH):
        for j in range(LENGTH):
            if i == j and not PUM[i][j] == None:
                raise InvalidInputException
            if i != j and not PUM[i][j] == PUM[j][i]:
                raise InvalidInputException


    FUV = []
    for i in range(LENGTH):
        if not PUV[i]: # FUV[i] is true if PUV[i] is false
           FUV.append(True)
        else: # or all elements of PUM[i] are true except PUM[i][i]
            unlock = True
            for j in range(LENGTH):
                if unlock and i != j and (not PUM[i][j]):
                    unlock = False
            FUV.append(unlock)
    return FUV
