#!/usr/bin/python2

import os

from os.path import join, getsize
def me():
	for root, dirs, files in os.walk('/home/chill/python/python/'):
		print root

me()
