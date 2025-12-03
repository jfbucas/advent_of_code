#!/usr/bin/python3

f = open("input", "r")

l  = f.readline()


l = list(l)
#print(l)

floor = 0
basement = None

counter = 1
for i in l:
	if i == "(":
		floor += 1
	elif i == ")":
		floor -= 1
	else:
		print("Error")

	if floor == -1 and basement == None:
		basement = counter

	counter += 1

print("Part one: ", floor)

print("Part two: ", basement)
