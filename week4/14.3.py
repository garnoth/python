#!/usr/bin/python2
##taken largly from the example program
import shelve
from anagram_sets import *

def store_anagrams(filename, ad):
	shelf = shelve.open(filename, 'c')
	
	for word, word_list in ad.iteritems():
		shelf[word] = word_list
	shelf.close()


def read_anagrams(filename, word):
	shelf = shelve.open(filename)
	sig = signature(word)
	try:
		return shelf[sig]
	except:
		print 'word not found'

def main(name, command='store'):
	if command == 'store':
		ad = all_anagrams('words.txt')
		store_anagrams('anagrams.db', ad)		
	else:
		print read_anagrams('anagrams.db', command)

main('name', 'stickler')
	
