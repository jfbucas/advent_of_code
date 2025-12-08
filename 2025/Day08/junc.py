#!/usr/bin/python3

import re
import sys
import itertools
import math
import multiprocessing as mp

sys.setrecursionlimit(150000)

around = [ (-1, 0), (-1, -1), (0, -1), (1,-1), (1,0), (1,1), (0,1), (-1,1) ]


junc = {}
f = open( sys.argv[1], "r" )
for l in f.readlines():
	junc[l.strip()] = list(map(int, l.strip().split(",")))

nb_loops = 10
if sys.argv[1] == "input":
	nb_loops = 1000

def dist(a,b):
	return (a[0]-b[0])*(a[0]-b[0]) + \
		(a[1]-b[1])*(a[1]-b[1]) + \
		(a[2]-b[2])*(a[2]-b[2])

# Precalcul
distances = {}
for sa in junc:
	for sb in junc:
		if sa == sb: continue
		if sa+"-"+sb in distances: continue
		if sb+"-"+sa in distances: continue
		distances[ sa+"-"+sb ] = (sa, sb, sa+"-"+sb, dist(junc[sa], junc[sb]))

sorted_distances = [ (k,v) for k,v in sorted(distances.items(), key=lambda x: x[1][3]) ]


# Part 1
connected = {}
groups = {}
group_count = 0

for l in range(nb_loops):

	shortest = 0
	while sorted_distances[shortest][0] in connected:
		shortest += 1
	
	connected[ sorted_distances[shortest][0] ] = True

	print(shortest)

	ja = sorted_distances[shortest][1][0]
	jb = sorted_distances[shortest][1][1]

	if ja in groups:
		if jb in groups:
			if groups[ja] != groups[jb]:
				# We need to propagate
				to_replace = groups[jb]
				for x in groups:
					if groups[x] == to_replace:
						groups[x] = groups[ja]
			else:
				# Already in the same group
				pass
		else:
			groups[jb] = groups[ja]
	else:
		if jb in groups:
			groups[ja] = groups[jb]
		else:
			groups[ja] = group_count
			groups[jb] = group_count
			group_count += 1

groups_size = []
for n in range(group_count):
	groups_size.append(len([x for x in groups if groups[x] == n]))
	
groups_size.sort()
print("Part1:", groups_size[-3]*groups_size[-2]*groups_size[-1])

# Part 2
connected = {}
groups = {}
no_groups = {}
group_count = 0

for j in junc:
	groups[j] = -1

has_no_group = len(junc)

while True:

	shortest = 0
	while sorted_distances[shortest][0] in connected:
		shortest += 1
	
	print(shortest)

	connected[ sorted_distances[shortest][0] ] = True
	

	ja = sorted_distances[shortest][1][0]
	jb = sorted_distances[shortest][1][1]

	if ja in no_groups:
		if jb in no_groups:
			if groups[ja] != groups[jb]:
				# We need to propagate
				to_replace = groups[jb]
				for x in groups:
					if groups[x] == to_replace:
						no_groups[x] = no_groups[ja]
						groups[x] = groups[ja]
			else:
				# Already in the same group
				pass
		else:
			no_groups[jb] = no_groups[ja]
			groups[jb] = groups[ja]
	else:
		if jb in no_groups:
			no_groups[ja] = no_groups[jb]
			groups[ja] = groups[jb]
		else:
			no_groups[ja] = group_count
			no_groups[jb] = group_count
			groups[ja] = group_count
			groups[jb] = group_count
			group_count += 1

	#print( len([x for x in groups if groups[x] == -1]) )
	if len([x for x in groups if groups[x] == -1]) == 0:
		break
	

print(ja, jb)
m = int(ja.split(',')[0]) * int(jb.split(',')[0])
print("Part2:", m)
