#!/usr/bin/python2

def any_lowercase1(s):
## returns True if the first letter in the word is lowercase
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
## returns the string "True" since 'c' is lowercase
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
## returns True if the last character in the word is lower case, if not, false
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
## this actually returns True is there are any lower case characters in the word
   flag = False
   for c in s:
        flag = flag or c.islower()
   return flag

def any_lowercase5(s):
# returns True only if all characters are lowercase
    for c in s:
        if not c.islower():
            return False
    return True


print any_lowercase5('aaaB')
