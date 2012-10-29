#!/usr/bin/python2

def gcd(a, b):
	if a == b:
		print 'Hey no fair,', a
	elif b == 0:
		print 'GCD is', a
	else:
		r = a % b
		gcd(b, r)

print gcd(1071,462)
