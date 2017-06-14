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

print("A:", numberA, "C:", numberC, "G:", numberG, "T:", numberT, "Total:", total)

perA = (numberA / total)
perC = (numberC / total)
perG = (numberG / total)
perT = (numberT / total)

print("First file" "\n" "%A:", perA, "\n" "%C:", perC, "\n" "%G:", perG, "\n" "%T:", perT)

InFile.close()

##Second file

filename2 = sys.argv[2]
InFile2 = open(filename2, 'r')


numberA2 = 0
numberC2 = 0
numberG2 = 0
numberT2 = 0	

for lines2 in InFile2:
	numberA2 += lines2.count('A')
	numberC2 += lines2.count('C')
	numberG2 += lines2.count('G')
	numberT2 += lines2.count('T')

total2 = numberA2 + numberC2 + numberG2 + numberT2

print("A:", numberA2, "C:", numberC2, "G:", numberG2, "T:", numberT2, "Total:", total2)

perA2 = (numberA2 / total2)
perC2 = (numberC2 / total2)
perG2 = (numberG2 / total2)
perT2 = (numberT2 / total2)

print("Second file" "\n" "%A:", perA2, "\n" "%C:", perC2, "\n" "%G:", perG2, "\n" "%T:", perT2)

InFile2.close()

calc = numpy.sqrt(((perA - perA2)**2 + (perC - perC2)**2 + (perG - perG2)**2 + (perT - perT2)**2)/4)

print(calc)







