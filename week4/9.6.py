#!/usr/bin/python2

def is_abecedarian(word):
##we are only looking for lower case words
	my_word = word.strip()
	last_letter = 'a'
	for l in word:
		if l < last_letter:
			return False
		last_letter = l
	return True	

prompt = "input a word, now\n"
user_input_a = raw_input(prompt)

print is_abecedarian(user_input_a)
