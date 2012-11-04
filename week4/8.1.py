#!/usr/bin/python2

def backwards(word):
	index = len(word)-1
	while index !=-1:
		letter = word[index]
		print letter
		index = index -1

backwards('pooperpants')
