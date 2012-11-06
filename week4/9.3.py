#!/usr/bin/python2

def avoids(word, chars):
	flag = False
	for l in chars:
		flag = flag or l in word
	return flag

#print avoids('me', 'cetwf')

prompt = "input a word. hit enter and enter all of the characters you want to check for\n"
user_input_a = raw_input(prompt)
user_input_b = raw_input('and the letters\n')

print avoids(user_input_a,user_input_b)
