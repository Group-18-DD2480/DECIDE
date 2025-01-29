def construct_PUM(LCM, CMV, LENGTH = 15):
    PUM = []
    for i in range(LENGTH):
        tempRow = []
        for j in range(LENGTH):
            tempRow.append(LCM[i][j](CMV[i], CMV[j]))
        PUM.append(tempRow)
    return PUM

def construct_FUV(PUM, PUV, LENGTH = 15):
    FUV = []
    for i in range(LENGTH):
        if not PUV[i]: # FUV[i] is true if PUV[i] is false
           FUV.append(True)
        else: # or all elements of PUM[i] is true
            FUV.append(all(PUM[i]))
    return FUV