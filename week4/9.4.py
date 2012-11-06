#!/usr/bin/python2

def uses_only(word, chars):
	for l in word:
		if not l in chars:
			return False
	return True


prompt = "input a word. hit enter and enter all of the letters that must beincluded in the word\n"
user_input_a = raw_input(prompt)
user_input_b = raw_input('and the letters\n')

print uses_only(user_input_a,user_input_b)
