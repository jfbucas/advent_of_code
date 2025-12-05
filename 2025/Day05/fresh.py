#!/usr/bin/python3

import re
import sys
import itertools
import math
import multiprocessing as mp

sys.setrecursionlimit(150000)

around = [ (-1, 0), (-1, -1), (0, -1), (1,-1), (1,0), (1,1), (0,1), (-1,1) ]


fresh_ranges = []
products = []
lines_ranges={}
f = open( sys.argv[1], "r" )
empty=False
for l in f.readlines():
	l = l.strip()
	if l == "":
		empty = True
		continue

	if not empty:
		if l not in lines_ranges:
			lines_ranges[l] = True
			[start, finish] = l.split("-")
			fresh_ranges.append( [int(start),int(finish)] )
	else:
		products.append(int(l))

#print(fresh_ranges)
#print(products)

# Part 1
total = 0
for p in products:
	for rs, rf in fresh_ranges:
		if p >= rs and p <= rf:
			total += 1
			break

print("Part1:", total)

total = 0
overlap = 0
for ras, raf in fresh_ranges:
	total += raf-ras+1

for [ras, raf], [rbs,rbf] in itertools.combinations(fresh_ranges, 2):
	if rbs >= ras and rbs <= raf:
		if rbf >= ras and rbf <= raf:
			#  ras----------------raf
			#       rbs------rbf
			overlap += rbf-rbs+1
		else:
			#  ras------raf
			#       rbs------rbf
			overlap += raf-rbs+1

	elif rbf >= ras and rbf <= raf:
		if rbs >= ras and rbs <= raf:
			print("HERE")
			overlap += rbf-rbs+1
		else:
			#      ras--------raf
			#  rbs------rbf
			overlap += rbf-ras+1
	else:
		print(ras,raf, rbs,rbf)

print("Part2:", total - overlap )
