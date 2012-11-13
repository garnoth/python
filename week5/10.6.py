#!/usr/bin/python2

b = [1,2,3]
c = [3,4,5,6,8,3]
d = ['a','b','c','a']

def is_sorted(lst):
	for i in range(len(lst)-1):
		if lst[i] > lst[i+1]:
			return False
	return True

print is_sorted(d)
