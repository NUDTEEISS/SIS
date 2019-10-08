#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import matlab
import matlab.engine
eng = matlab.engine.start_matlab()
Keys = matlab.uint8(Keys)
Shares = matlab.uint8(Shares)
S = eng.Recover(2,2,Keys,Shares)
Secrets = list(S[0])
# print eng.triarea(1.0,5.0)