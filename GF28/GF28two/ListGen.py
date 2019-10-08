#!/usr/bin/env python
# -*- coding: utf-8 -*-

#**************************************************
#Generate the list and inverse list for different Galois Prime
#**************************************************

#There are 15 primitive polynomials in Galois field (2^8)
PrimitivePolys = [285, 299, 301, 333, 351, 355, 357, 361, 369, 391, 425, 451, 463, 487, 501]
#Generator = x
Generator = 2

#Calculate the next Power of x in the Galios Field (2^Power)
def CalcNextPower(CurPower, PrimitivePoly, Power):
    NextPower = (CurPower << 1)
    if NextPower >= 2**Power:
        NextPower = NextPower ^ PrimitivePoly
    return NextPower

#Generate the obverse list of all elements in Galios field, except 0.
def ObverseListGen(PrimitivePoly = 285, Power = 8, Generator = 2):
    ObverseList = [1, Generator]

    CurPower = Generator

    for i in range(2**Power - 3):
        NextPower = CalcNextPower(CurPower, PrimitivePoly, Power)
        ObverseList.append(NextPower)
        CurPower = NextPower
    print "ObverseList_{0} = ".format(PrimitivePoly)
    print ObverseList
    return ObverseList


def ReverseListGen(PrimitivePoly = 285, Power = 8, Generator = 2):
    ObverseList = ObverseListGen(PrimitivePoly, Power, Generator)
    ReverseList = [PrimitivePoly]
    for i in range(1, 256):
        ReverseList.append(ObverseList.index(i))
    print "ReverseList_{0} = ".format(PrimitivePoly)
    print ReverseList
    return ReverseList




# Check whether there exists the same elements in the list.
def CheckSameValues(GaloisList):
    Duplicates = []
    print len(GaloisList)
    for i in range(len(GaloisList)):
        LastValue = GaloisList.pop()
        for j in range(len(GaloisList)):
            if LastValue == GaloisList[j]:
                Duplicates.append(LastValue)
    print "There are {0} same values!!!".format(len(Duplicates))
    print Duplicates


# CheckSameValues(ListGen())
# ListGen(PrimitivePoly = 19, Generator =2,Power=4)


# ObverseListGen()
# ReverseListGen(285)
