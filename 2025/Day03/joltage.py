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


def part2_recursive(bank, before, start_index, max_combo):
	if start_index > len(bank):
		return max_combo

	depth = len(before)
	if depth == 12:
		return before

	# The option to skip the current digit
	max_combo = part2_recursive(bank, before, start_index+1, max_combo)

	# Or try all the current digits
	for i, n in bank[start_index:]:
		if int(n) >= int(max_combo[depth]):
			max_combo = part2_recursive(bank, before+n, i+1, max_combo)
	
	return max_combo


def bank_worker(bank):
	return part2_recursive(bank, "", 0, "0"*12)

# Part 2 
total = 0
processes = max(1, mp.cpu_count() - 1)

pool = mp.Pool(processes)

try:
	results_iter = pool.imap_unordered(bank_worker, banks)
	for max_combo in results_iter:
		total += int(max_combo)
		print(total)

finally:
	pool.close()
	pool.join()

print("Part2:", total)
