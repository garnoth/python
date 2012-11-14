#!/usr/bin/python2
##largly taken from the book

def most_frequent(mystr):

 	hist = make_histogram(mystr)
	t = []
	for x, freq in hist.iteritems():
		t.append((freq, x))
	t.sort(reverse=True)
	
	res = []
	for freq, x in t:
		res.append(x)
	return res


def make_histogram(s):
    """Make a map from letters to number of times they appear in s.

    s: string

    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


print most_frequent('hehehehehhe')
