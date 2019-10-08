#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cv2
from numpy import *
from Sharing import PolySharing
#*****************************************************************************************************
def imsharing(k,n,Keys):
    for p in range(n):#创建n个影子图像的数组
        locals()['share'+str(p)]=[[] for i in range(256)]
    image='W:\code\image\G_indor256.bmp'
    imatrix=cv2.imread(image,-1)#读取图像为矩阵
    #生成影子图像
    for i in range(256):
        for j in range(256):
            shares = PolySharing(imatrix[i][j], k, n,Keys)#每个像素点生成n个像素的数组
            for p in range(n):
                locals()['share' + str(p)][i].append(shares[p])
    for i in range(n):
        cv2.imwrite(r"shares\share"+str(Keys[i])+".bmp", mat(locals()['share'+str(i)]))
#*****************************************************************************************************
imsharing(2,3,[1,2,3])