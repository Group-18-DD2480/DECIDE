def PUM(LCM, CMV, LENGTH = 15):
    PUM = []
    for i in range(LENGTH):
        tempRow = []
        for j in range(LENGTH):
            tempRow.append(LCM[i][j](CMV[i], CMV[j]))
        PUM.append(tempRow)
    return PUM
