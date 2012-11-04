#!/usr/bin/python2

def is_palindrome(word1):
	if word1 == word1[::-1]:
		print 'Yes it is'
	else:
		print 'no it isn\'t'

is_palindrome('allen')
is_palindrome('bob')
is_palindrome('otto')
is_palindrome('redivider')
