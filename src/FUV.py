def FUV(PUM, PUV, LENGTH = 15):
    FUV = []
    for i in range(LENGTH):
        if not PUV[i]: # FUV[i] is true if PUV[i] is false
           FUV.append(True)
        else: # or all elements of PUM[i] is true
            FUV.append(all(PUM[i]))
    return FUV
