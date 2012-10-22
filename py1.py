#!/usr/bin/python2
def is_triangle(a,b,c):
	if a > b + c :
		print 'No, we cannot form a triangle'
	elif a == b + c :
		print 'Degenerate' #denegrate triangle
#so a is not greater then or equal to the sum of a and b
	else:
		print 'Yes, we can form a triangle'


def tri(n):
  if n <=0:
    return
  elif n==3:
    is_triangle(user_input_a,user_input_b,user_input_c)
  elif n==2:
    is_triangle(user_input_b,user_input_c,user_input_a)
  elif n==1:
    is_triangle(user_input_c,user_input_b,user_input_a)
  tri(n-1)



prompt = "please legnths of a triangle starting with the first size\n"
user_input_a = int(raw_input(prompt))
user_input_b = int(raw_input('and the second\n'))
user_input_c = int(raw_input('and the third\n'))
tri(3)
