#!/usr/bin/python2


def check_fermat(a,b,c,n):
        if a**n+b**n == c**n:
                print "Holy Smokes! He was wrong!!!"
        else:
                print "No, that doesn't work."


prompt = "please values to check ferments theorm. Start with A\n"
user_input_a = int(raw_input(prompt))
user_input_b = int(raw_input('and b\n'))
user_input_c = int(raw_input('and c\n'))
user_input_e = int(raw_input('and the exponent\n'))

print check_fermat(user_input_a,user_input_b,user_input_c,user_input_e)

