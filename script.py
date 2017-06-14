#! /usr/bin/env python3

import sys
import numpy
import argparse

filename = sys.argv[1]

InFile = open(filename, 'r')

numberA = 0
numberC = 0
numberG = 0
numberT = 0

for lines in InFile:
	numberA += lines.count('A')
	numberC += lines.count('C')
	numberG += lines.count('G')
	numberT += lines.count('T')

total = numberA + numberC + numberG + numberT

#print("A:", numberA, "C:", numberC, "G:", numberG, "T:", numberT)

perA = (numberA / total)*100
perC = (numberC / total)*100
perG = (numberG / total)*100
perT = (numberT / total)*100

print("%A:", perA, "\n" "%C:", perC, "\n" "%G:", perG, "\n" "%T:", perT)

InFile.close()
