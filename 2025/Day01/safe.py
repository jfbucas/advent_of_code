#!/usr/bin/python3

import re
import sys
import itertools
import math

sys.setrecursionlimit(150000)

l = []
f = open( sys.argv[1], "r" )
for line in f.readlines():
	line=line.strip()

	d = line[0]
	n = int(line[1:])
	l.append( (d,n) )

# Part 1
position = 50
code = 0
for direction,num in l:
	new_position = position

	if direction in ["R"]:
		new_position = (position + num) % 100
		if new_position == 0:
			code += 1
			
	elif direction in ["L"]:
		new_position = (position - num) % 100
		if new_position == 0:
			code += 1

	position = new_position

	print(position)

print("Part1:", code)

# Part 2
position = 50
code = 0
for direction,num in l:
	new_position = position

	if direction in ["R"]:
		new_position = (position + num)
		#if new_position // 100 != 0:
		code += -((position+num) // -100)
			
	elif direction in ["L"]:
		new_position = (position - num)
		#if new_position // 100 != 0:
		code += -((position-num) // -100)

	position = new_position % 100

	print(position)

print("Part2:", code)
