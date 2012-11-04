#!/usr/bin/python2

def rotate_word(word, rotation):
	new_word = ''
	for x in word:
		new_word = new_word +  chr(ord(x)+rotation)
	print new_word
rotate_word('melon', -10)

