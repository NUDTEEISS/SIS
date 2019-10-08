#!/usr/bin/env python
# -*- coding:utf-8 -*-
from AllList import ObverseList_285 as ObverseList
from AllList import ReverseList_285 as ReverseList
def mul(a,b):
    if a== 0 or b == 0:
        return 0
    c = ObverseList[(ReverseList[a]+ReverseList[b])%255]
    return c
def div(a,b):
    if a== 0:
        return 0
    c = ObverseList[(ReverseList[a]-ReverseList[b])%255]
    return c