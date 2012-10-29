#!/usr/bin/python2

def is_power(a, b):
	"""checks to see if a is a power of b"""
	if a % b != 0:
	#is a divisible by b?
		return False
	else:
		is_power((a/b), b)
		return True


print (is_power(8,4))

