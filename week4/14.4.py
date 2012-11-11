#!/usr/bin/python2

import os

def walk(dirname):
	"""Prints the names of all files in dirname and its subdirectories.
	dirname: string name of directory
	"""
	for name in os.listdir(dirname):   

		path = os.path.join(dirname, name)
		if os.path.isfile(path):
			if path.endswith('mp3'):			
				cmd = 'md5sum'
				fp = os.popen(cmd +' '+ path)
				res = fp.read()
				print res.split(" ")[0]
				fp.close()
		
		else:
			walk(path)


walk('/home/chill/python/python/week4')
