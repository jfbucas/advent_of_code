#!/usr/bin/python3

import re
import sys
import itertools
import math

sys.setrecursionlimit(150000)

l = []
f = open( sys.argv[1], "r" )
line = f.readline()
line = line.strip()
ranges = line.split(",")


for r in ranges:
	print(r)
	s = r.split("-")
	l.append( (int(s[0]), int(s[1])) )

#print(l)

# Part 1
if False:
	in_id = 0
	for i in range(0, 100000):
		for start, finish in l:
			s = int(str(i)*2)
			if s >= start and s <= finish:
				print(i, s, start, finish)
				in_id += s


	print("Part1:", in_id)

# Part 2
in_id = []
for start, finish in l:
	for i in range(0, 100000):
		for repeat in range(2,8):
			s = int(str(i)*repeat)
			if s >= start and s <= finish:
				if s not in in_id:
					print(i, s, start, finish)
					in_id.append( s )


print("Part2:", sum(in_id))
