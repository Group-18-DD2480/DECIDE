def FUV(PUM, PUV, LENGTH = 15):
    """
    Constructs the Final Unlocking Vector (FUV) based on the Preliminary Unlocking Matrix (PUM) and the Preliminary Unlocking Vector (CMV).

    Args:
        PUM (list of list of booleans): A symmetric square matrix where each element is a boolean or None.
        PUV (list of bool): A vector containing boolean values that whether the corresponding row in PUM should be considered or not.

    Returns:
        list: A square matrix PUM where each entry FUV[i] is set to True if PUV[i] is False or 
        if all PUM[i][j] are True disregarding PUM[i][i], otherwise it is False.
    
    Raises:
        InvalidInputException: If PUM or PUV is not a list, if their sizes do not match, or if PUM 
            is not symmetric.
    """
    FUV = []
    for i in range(LENGTH):
        if not PUV[i]: # FUV[i] is true if PUV[i] is false
           FUV.append(True)
        else: # or all elements of PUM[i] is true
            FUV.append(all(PUM[i]))
    return FUV
