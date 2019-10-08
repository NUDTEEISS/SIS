#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cv2
from numpy import mat
from Recover import PolyRecovering
def imrecover(Keys):
    l = len(Keys)
    for i in range(l):
        globals()['share'+str(i)] = 'shares\share'+str(Keys[i])+'.bmp'
    # share2='share2.bmp'
        globals()['rematrix' + str(i)]=cv2.imread(globals()['share'+str(i)],-1)
    # rematrix2=cv2.imread(share2,-1)
    recover = [[] for i in range(256)]
    for i in range(256):
        for j in range(256):
            shares = []  # serial tuple
            for p in range(l):
                shares.append(globals()['rematrix' + str(p)][i][j])
            rec = PolyRecovering(shares, Keys)
            recover[i].append(rec)
    cv2.imwrite(r"shares\recover.bmp", mat(recover))
imrecover([1,2])