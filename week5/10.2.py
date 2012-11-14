#!/usr/bin/python2

def capitalize_all(t):
	res = []
	for s in t:
		if type(s) == list:
			res.append(capitalize_all(s))
		else:
			res.append(s.capitalize())
	return res

c = ['hehe',['de','do'],'hoho','haha']

print capitalize_all(c)
