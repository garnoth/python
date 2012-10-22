#!/usr/bin/python2


import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)



def koch(t, legnth):
	if legnth < 3:
		fd(t, legnth)
		return
	angle = 60
	koch(t,legnth/3)
	lt(t, angle)
	koch(t,legnth/3)
	rt(t, 2*angle)
	koch(t, legnth/3)
	lt(t, angle)
	koch(t, legnth/3)


def snowflake(t, legnth):
	for i in range (3):
		koch(t, legnth)
		rt(t, 120)

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001

    # draw a circle centered on the origin
#    draw(bob, 10,10)
#    koch(bob, 100)
    snowflake(bob, 1000)
    wait_for_user()

