#!/usr/bin/python3

import re
import sys
import itertools
import math
import multiprocessing as mp

sys.setrecursionlimit(150000)

banks = []
f = open( sys.argv[1], "r" )
for l in f.readlines():
	l = l.strip()
	banks.append( list(zip( range(len(l)), list(l))) )

# Part 1
total = 0
for bank in banks:
	max_combo = -1
	for (i1, n1) in bank:
		for (i2, n2) in bank[i1+1:]:
			combo = int(str(n1)+str(n2))
			if combo > max_combo:
				max_combo = combo

	total += max_combo

print("Part1:", total)


def part2_recursive(bank, before, index):
	
	if len(before) == 12:
		return before

	l = []
	for i, n in bank[index:]:
		l.append( (i,n) )

	l.sort(key=lambda x: (x[1], -x[0]))

	for i, n in reversed(l):
		m = part2_recursive(bank, before+n, i+1)
		if m != None:
			return m

	return None


# Part 2 
total = 0
for bank in banks:
	total += int(part2_recursive(bank, "", 0))

print("Part2:", total)
