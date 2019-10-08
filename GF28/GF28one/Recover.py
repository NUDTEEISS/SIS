#!/usr/bin/env python
# -*- coding: utf-8 -*-
from computer import *

def PolyRecovering(Shares, Keys):
    # free_coefficient = modular_lagrange_interpolation(0, points, prime)
    Secret = 0
    sharenum = len(Shares)
    for i in range(sharenum):
        nu, de = 1,1#numerator/denominator分子和分母
        for j in range(sharenum):
            if i == j:
                continue
            nu = mul(nu , (0^Keys[j]))
            de = mul(de , (Keys[i]^Keys[j]))
        Secret = Secret ^ mul(Shares[i] , div(nu,de))
    return Secret
# print PolyRecovering([116,203,85], [1,2,3])


