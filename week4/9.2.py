#!/usr/bin/python2

def fit():
#iterate through a file. Pass the word off to has_no_e
	f = open('words.txt', 'r')
	no_e_count = 0
	count = 0
	for line in f:
		word = line.strip()
		if has_no_e(word):
			count = count + 1
			no_e_count = no_e_count +1
		else:
			count = count + 1
	f.close()
	#print no_e_count
	#print count
	print  100.0 * no_e_count / count
def has_no_e(word):
	if 'e' in word:
		return False
	else: 
		return True


fit()
