#!/usr/bin/env python
# -*- coding: utf-8 -*-
from computer import *
# generate key产生n个序号
def ReduceSharing(Secrets, k, n, Keys):
    shares=[]
    for i in range(n):
        sum = 0
        for j in range(k-1,-1,-1):
            sum = Secrets[j] ^ mul(sum,Keys[i])
        shares.append(sum)
    return shares
