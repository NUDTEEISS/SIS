#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
from numpy import *
from Sharing import ReduceSharing
def imsharing(k,n,Keys):
    image='G_man256.bmp'
    imatrix=cv2.imread(image,-1)#读取图像
    for p in range(n):#创建n个影子图像的数组
        locals()['share'+str(p)]=[[] for i in range(256)]
    for i in range(256):
        for j in range(256/k):
            shares=ReduceSharing(imatrix[i][k*j:k*j+k], k, n,Keys)
            for p in range(n):
                locals()['share' + str(p)][i].append(shares[p])
    for i in range(n):
        cv2.imwrite(r"shares\share"+str(Keys[i])+".bmp", mat(locals()['share'+str(i)]))