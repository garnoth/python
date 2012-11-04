#!/usr/bin/python2

def find(word, letter, start_index):
    index = start_index
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print find('piecesx', 'p', 0)
