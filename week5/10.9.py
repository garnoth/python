#!/usr/bin/python2

import random
str = ['a','b','b','a']

def remove_duplicates(word):
	set = []
	for x in range(len(word)):
		if word[x] not in set:
			set.append(word[x])
	return set

print remove_duplicates(str)

