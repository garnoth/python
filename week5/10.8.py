#!/usr/bin/python2

import random
str = [1,2,5,3,4,5]
str2 = 'hannah1'

def has_duplicates(word):
	mylst = word
	mylst.sort()
	for i in range(len(mylst)-1):
		if mylst[i] == mylst[i+1]:
			return False
	return True

#print has_duplicates(str)


def twentythree():
	for i in range (0,24):
		print random.randint(1,10)

twentythree()
