#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
from numpy import mat
import matlab.engine
eng = matlab.engine.start_matlab()
def imrecover(Keys,k):
    l = len(Keys)
    for i in range(l):
        globals()['share'+str(i)] = 'shares\share'+str(Keys[i])+'.bmp'
        globals()['rematrix' + str(i)]=cv2.imread(globals()['share'+str(i)],-1)
    recover = [[] for i in range(256)]
    Keys = matlab.uint8(Keys)
    for i in range(256):
        for j in range(256/k):
            shares = []  # serial tuple
            for p in range(l):
                shares.append(globals()['rematrix' + str(p)][i][j])
            Shares = matlab.uint8(shares)
            S = eng.Recover(k,Keys,Shares)
            Secrets = list(S[0])
            for q in range(k):
                recover[i].append(Secrets[q])
    cv2.imwrite(r"shares\recover.bmp", mat(recover))