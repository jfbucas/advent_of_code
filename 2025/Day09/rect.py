#!/usr/bin/python3

import re
import sys
import itertools
import math
import multiprocessing as mp

sys.setrecursionlimit(150000)

around = [ (-1, 0), (-1, -1), (0, -1), (1,-1), (1,0), (1,1), (0,1), (-1,1) ]


tiles = {}
f = open( sys.argv[1], "r" )
for l in f.readlines():
	l = l.strip()
	[x,y] = map(int,l.split(","))
	tiles[str(x)+","+str(y)] = (x, y)


# Part 1
total = 0
max_size = 0
for ta in tiles:
	for tb in tiles:
		if ta == tb:
			continue
		xa,ya = tiles[ta]
		xb,yb = tiles[tb]


		size = abs(xa-xb+1)*abs(ya-yb+1)
		print(xa,ya, " ", xb,yb, " ", size)
		if size > max_size:
			max_size = size

print("Part1:", max_size)
exit()


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
