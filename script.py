#! /usr/bin/env python3
import sys
import numpy
import argparse

filename = open (sys.argv[*], 'r')

numberA = filename.count(A)
numberC = filename.count(C)
numberG = filename.count(G)
numberT = filename.count(T)
total = numberA + numberC + numberG + numberT

perA = numberA / total
perC = numberC / total
perG = numberG / total
perT = numberT / total

print(perA)
print(perC)
print(perG)
print(perT)
