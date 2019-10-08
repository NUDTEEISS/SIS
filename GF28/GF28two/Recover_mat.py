#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from MatrixInverse import Inverse_Matrix
import matlab.engine
eng = matlab.engine.start_matlab()
#Generate the inverse Matrix in corresponding to Serials
# 生成范德蒙德矩阵
def Matrix_Generate(Serials, k):
    matrix = []
    for serial in Serials:
        row = []
        for i in range(k):
            row.append(serial ** i)
        matrix.append(row)
    return matrix
#Based on Matrix, solve the recovered value
def Shamir_Recovering_Matrix(Shares, Serials, k):
    #Generate the square matrix based on serials and k.
    matrix = np.matrix(Matrix_Generate(Serials, k))
    #Make a solvable square matrix according to shares and k.
    if len(Shares) > k:
        Shares = Shares[:k]
        matrix = matrix[:k, :]
    else:
        matrix = matrix[ : ,:len(Shares)]
    #Compute the Inverse Matrix of coefficient matrix
    gfmatrix = eng.gf(matrix,8)
    gfShares = eng.gf(Shares,8)
    InverseMatrix = eng.inv(gfmatrix)
    #Solve the Recovered values.
    RecoveredPixels = InverseMatrix*gfShares

    # SecretPixel = RecoveredPixels[0]
    return RecoveredPixels
print Shamir_Recovering_Matrix([123,212],[1,2],2)