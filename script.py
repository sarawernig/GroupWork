#! /usr/bin/env python3
import sys
import numpy
import argparse

fin = open (sys.argv[*], 'r')
for line in fin:
    lines = line.rstrip('\n')
    if line[0] == '>':
       name = line
       id.append(name)
    else:
       sequence += line

