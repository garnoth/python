#!/usr/bin/python2
t = [[1,2,3], 3, [1,4,3]]
b = [1,2,3,4]


def middle(lst):
	del lst[0]
	del lst[-1]
	return lst

print middle(b)
