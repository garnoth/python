#!/usr/bin/python2


def sed(input1, input2, file1, file2):
    try:
        f = open(file1, r)
        for line in f:
            print line
        f.close()
    except:
        print "woah, something happened? Perhaps the file didn't exist"

#sed('m','e','me.txt', 'w')

def sed(i1, i2, filename, outfile):
	try:
		f = open(filename)
		for line in f:
			print line
	except:
		print "eek"

sed('1', '2', 'me.txt', '3')
