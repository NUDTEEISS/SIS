#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Imsharing import *
from Imrecover import *
import time
k=2
n=2
Keys = [1,2]
start = time.clock()
imsharing(k,n,Keys)
time1 = time.clock() - start
# imrecover(Keys,k)
# time2 = time.clock() - start
print "share:",time1
# print "recover:",time2-time1
# imrecover(Keys)