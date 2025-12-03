#!/usr/bin/python3

import re
import sys
import itertools
import math

sys.setrecursionlimit(150000)

banks = []
f = open( sys.argv[1], "r" )
for l in f.readlines():
	l = l.strip()
	banks.append( list(zip( range(len(l)), list(l))) )

print(banks[0])
#print(banks[0][5:])
#exit()


# Part 1
total = 0
for bank in banks:
	max_combo = -1
	for (i1, n1) in bank:
		for (i2, n2) in bank[i1+1:]:
			combo = int(str(n1)+str(n2))
			if combo > max_combo:
				max_combo = combo

	#print(max_combo)
	total += max_combo

print("Part1:", total)


def part2_rec(bank, before, start, max_combo):
	if len(before) == 12:
		print("New MAX: ", before)
		return int(before)

	partial_max_combo = int(str(max_combo)[0:len(before)+1])
	print(partial_max_combo, " --")
	for i, n in bank[start:]:
		combo = int( (before+n) ) #.ljust(12, "0") )
		print(combo, ">=", partial_max_combo )
		if combo >= partial_max_combo:
			max_combo = part2_rec(bank, before + str(n), i+1, int( (before+n).ljust(12, "0") ))
	return max_combo


# Part 2 Ugly Do not attempt at home kids
total = 0
for bank in banks:
	max_combo = part2_rec(bank, "", 0, int("1"*12))
	print(max_combo)
	total += max_combo

print("Part2:", total)
