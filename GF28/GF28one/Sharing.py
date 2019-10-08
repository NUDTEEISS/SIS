#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import random
from computer import *

def PolySharing(Secret, k, n, Keys):
    cfs = [Secret]#coefficients
    for i in range(k-1):
        cfs.append(random.choice(range(0, 255)))#产生k-1个随机数
    shares = []
    for i in range(n):
        sum = 0
        for j in range(k-1,-1,-1):
            sum = cfs[j] ^ mul(sum,Keys[i])
        shares.append(sum)
    return shares
# print PolySharing(234,2,3,[1,2,3])

