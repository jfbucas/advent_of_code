#!/usr/bin/python3

import re
import sys
import itertools
import math
import multiprocessing as mp

sys.setrecursionlimit(150000)

around = [ (-1, 0), (-1, -1), (0, -1), (1,-1), (1,0), (1,1), (0,1), (-1,1) ]


numbers = []
ops = []
f = open( sys.argv[1], "r" )
for l in f.readlines():
	l = l.strip()
	while "  " in l:
		l = l.replace("  "," ")
	l = l.split(" ")
	if l[0] in [ "+", "*" ]:
		ops = l
		continue

	numbers.append(list(map(int, l)))

#print(numbers)
#print(ops)

# Part 1
total = 0
for c in range(len(numbers[0])):
	mathz = int(ops[c] == "*")
	for r in range(len(numbers)):
		exec("mathz "+ops[c]+"= numbers[r][c]")

	total+=mathz

print("Part1:", total)



ops = []
f = open( sys.argv[1], "r" )
for l in f.readlines():
	l = l.strip('\n')
	if l[0] in [ "+", "*" ]:
		ops = l

all_lines=[]
f = open( sys.argv[1], "r" )
for l in f.readlines():
	l = l.strip('\n')
	if l[0] in [ "+", "*" ]:
		continue
	all_lines.append(l)

total = 0
numbers = []
for c in reversed(range(len(ops))):
	n = ""
	for r in range(len(all_lines)):
		n+=all_lines[r][c]

	n = n.strip()
	if n != "":
		n = int(n)
		numbers.append(n)
	
	if ops[c] in ["+", "*"]:
		total += eval(ops[c].join(map(str,numbers)))
		numbers = []


print("Part2:", total )
