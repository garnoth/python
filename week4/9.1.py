#!/usr/bin/python2

f = open('words.txt', 'r')
#read through the word list, printing only words longer than 20 chars
for line in f:
	word = line.strip()
	if len(word) > 20:
		print word
	
f.close()
