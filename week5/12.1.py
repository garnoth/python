#!/usr/bin/python2

def sumall(*args):
	total = 0
	t = tuple(args)
	for x in range (len(t)):
		total += t[x]
	return total

print sumall(1,2,3,4)
