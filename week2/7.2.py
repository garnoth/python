#!/usr/bin/python2

def square_root(a):
	# compute the square of a
	x = a/2.0
	while True:	
		print x
		y = (x + a/x) / 2
		if abs(y-x) < 0.000001:
			break
		x = y
	print 'our estimate is:', x

square_root(102)
