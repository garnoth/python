#!/usr/bin/python2
t = [[1,2,3], 3, [1,4,3]]
b = []


def cuml_sum(lst):
#this returns a list of the cumulative sum for the given list
	res = []
	for i in range(len(lst)):
		res.append(sum(lst[0:i+1]))
	return res

print cuml_sum(b)
