#!/usr/bin/python2

def find(word, letter, start_index):
### search a string for a letter and keep a counter, optional start offset
    index = start_index
    count = 0
    while index < len(word):
        if word[index] == letter:
             count = count + 1
        index = index + 1
    print count

find('beaaxaeaaaar', 'x', 0)
