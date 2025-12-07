#!/usr/bin/python3

import re
import sys
import itertools
import math
import multiprocessing as mp

sys.setrecursionlimit(150000)

around = [ (-1, 0), (-1, -1), (0, -1), (1,-1), (1,0), (1,1), (0,1), (-1,1) ]


start = None
splitters = {}
beams = []
y = 0
f = open( sys.argv[1], "r" )
for l in f.readlines():
	x = 0
	l = l.strip()
	for x in range(len(l)):
		if l[x] in [ "S" ]:
			start = [x,y]
		elif l[x] in [ "^" ]:
			splitters[ str(x)+"_"+str(y) ] = True
	y+=1
height = y
#print(start)
#print(splitters)

beams = [ start ]

# Part 1
nb_split = 0
while len(beams) > 0:
	#print(beams)
	for b in beams:
		if str(b[0])+"_"+str(b[1]) in splitters:
			#print("split", b)
			# Add the two new beams
			if [b[0]-1, b[1]] not in beams:
				beams.append( [b[0]-1, b[1]] )
			if [b[0]+1, b[1]] not in beams:
				beams.append( [b[0]+1, b[1]] )
			# Remove the original one
			b[1] = height+1
			nb_split += 1

	# Keep only the beams still on the map
	beams = [ [x,y+1] for (x,y) in beams if y <= height ]

print("Part1:", nb_split)
