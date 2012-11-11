#!/usr/bin/python2
t = [[1,2,3], 3, [1,4,3]]
b = [1,2,3]

def nested_sum(lst):
# this will return the sum of all nested lists, calling itself again if the item is a list
	total = 0
	for x in lst:
		if type(x) == list:
			total += nested_sum(x)
		else:
			total += x
	return total

print nested_sum(t)
