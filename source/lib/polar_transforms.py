##  Isolation Pong Transforms Library
##  @version 0.01
##  @author Mathew Murgatroyd <mathewmurgatroyd@gmail.com>

## This file takes cartesian coordinates and transforms them into polar coordinates and vice versa
## All inpus and outputs are in degrees

import math

def polarToCart(rad,ang):
    ang = ang*(math.pi/180) # takes angle in degrees and turns to rads
    x = rad*(math.cos(ang)) # finds x and y coordinates through trig
    y = rad*(math.sin(ang))
    return (x, y)

def cartToPolar(x,y):
    rad = math.sqrt((y*y)+(x*x)) # find hyp/ radius
    if x < 0 and y > 0 :
        ang = 180 - abs((math.asin(y/rad)*(180/math.pi))) # takes x and y coordinates and finds angle, converted into degrees
    elif x > 0 and y < 0:
        ang = 360 - abs((math.asin(y/rad)*(180/math.pi)))
    elif x < 0 and y < 0:
        ang = 180 + abs((math.asin(y/rad)*(180/math.pi)))
    elif y == 0 :
        ang = 0
    else:
        ang = abs((math.asin(y/rad)*(180/math.pi)))

    return (rad, ang)
