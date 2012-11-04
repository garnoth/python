#!/usr/bin/python2
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
##fix for Ouack and Quack
	if letter == 'O' or letter == 'Q':
		print letter + 'u' + suffix

	print letter + suffix
