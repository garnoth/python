#!/usr/bin/python2

def sed(target, pattern, filename, outfile):
##replaces target with pattern, reading from filename and writing to outfile
	try:
		f = open(filename, 'r')
		fout = open(outfile, 'w')
	except:
		print "eek, somethings wrong. I probably couldn't open the target file"
		return
	for line in f:
		if target in line:		
			fout.write(line.replace(target, pattern))
		else:
			fout.write(line)
	
	f.close()
	fout.close()
sed('peter', 'hannah', 'me.txt', 'out.txt')
