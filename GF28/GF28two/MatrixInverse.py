#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    Compute the inverse matrix of a matrix.
'''
import numpy as np
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
#模逆
def mod_inverse(k, prime):
    k = k % prime
    if k < 0:
        r = egcd(prime, -k)[2]
    else:
        r = egcd(prime, k)[2]
    return (prime + r) % prime
#求伴随矩阵
def BanSui(miniK):
    row = miniK.shape[0]
    column = miniK.shape[1]
    #只有方阵才能求解伴随矩阵
    if row != column:
        raise Exception("not square,No Bansui!")
    A = []
    for i in range(0, row):
        for j in range(0, column):
            i_index = range(0, i)
            i_index2 = range(i + 1, row)
            i_index.extend(i_index2)

            j_index = range(0, j)
            j_index2 = range(j + 1, column)
            j_index.extend(j_index2)
            juzhen = miniK[np.ix_(i_index, j_index)]
            # Mij 为代数余子式
            Mij = int(round(np.linalg.det(juzhen).item()))
            # Mij = int(np.linalg.det(juzhen))
            Aij = ((-1) ** (i + j)) * Mij
            A.append(Aij)
    mat = np.matrix(A)
    mat = mat.reshape((row, column))
    bansui = mat.T
    return bansui
#求出所有组合的逆矩阵，相当于表格，存储在inverseKList中，便于查找
def Inverse_Matrix(matrix, prime = 257):
    Matrix = np.matrix(matrix)
    (row, column) = Matrix.shape
    detValue = int(round(np.linalg.det(Matrix).item()))
    if (detValue < 0):
        detValue = detValue % prime
    #求伴随矩阵
    bansuiMatrix = BanSui(Matrix)
    #求行列式的模逆
    detModInv = mod_inverse(detValue, prime)
    #模逆乘伴随矩阵，得到逆矩阵
    InverseMatrix = (detModInv * bansuiMatrix) % prime
    return InverseMatrix

