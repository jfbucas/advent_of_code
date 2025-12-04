#!/usr/bin/python3

import re
import sys
import itertools
import math
import multiprocessing as mp

sys.setrecursionlimit(150000)

around = [ (-1, 0), (-1, -1), (0, -1), (1,-1), (1,0), (1,1), (0,1), (-1,1) ]


rolls_dict = {}
f = open( sys.argv[1], "r" )
y = 0
for l in f.readlines():
	l = l.strip()
	x = 0
	for s in l:
		if s == "@":
			rolls_dict[str(x)+","+str(y)] = (x, y)
		x += 1
	y += 1

height = y-1
width = x-1

initial_total_rolls = len(rolls_dict)

# Part 1
total = 0
for x,y in rolls_dict.values():
	n = 0
	for ax, ay in around:
		if str(x+ax)+","+str(y+ay) in rolls_dict:
			n+=1
	if n < 4:
		total +=1 
	

print("Part1:", total)


to_remove = [None]
while len(to_remove) > 0:
	to_remove = []
	for x,y in rolls_dict.values():
		n = 0
		for ax, ay in around:
			if str(x+ax)+","+str(y+ay) in rolls_dict:
				n+=1
		if n < 4:
			to_remove.append(str(x)+","+str(y))

	for r in to_remove:
		del rolls_dict[r]
	

print("Part2:", initial_total_rolls - len(rolls_dict) )
