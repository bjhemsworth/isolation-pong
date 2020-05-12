##
##  Isolation Pong Transforms Library Test script
##  @version 0.01
##  @author Mathew Murgatroyd <mathewmurgatroyd@gmail.com>

## This file tests the functions defined in the Transforms library against a range of imputs
## Function outputs are checked agaisnt result given by WOLFRAMALPHA and the results reports as pass if they are with 1% of expected value.

import sys
sys.path.append('../source')
from lib.polar_transforms import *

# build list of cartesian coordinates [[x1,x2..],[y1,y2...]]
cartList=[[-1,1,0.3,-0.2,-0.3,0.1,-0.6,0.9,-0.3,0.8],[0.7,0.2,-0.3,-0.6,-0.7,0.2,0.7,-0.4,0.4,-0.7]]

#build list of coresponding polar Coordinates [[r1,r2...][phi1,phi2...]]
polarList=[[1.221,1.020,0.424,0.6325,0.762,0.224,0.922,0.985,0.5,8],[145.008,11.310,360-45.000,360-108.435,360-113.199,63.435,130.601,360-23.962,126.8699,6]]

print("testing Transformations Libray")
print("## NOTE Q 9 IS DESIGNED TO FAIL ##")
print("Testing Polar to Cartesian Coordinates")
for i in range (0, len(cartList[0])):
    (x, y) = polarToCart(polarList[0][i],polarList[1][i])
    answerX = cartList[0][i]
    answerY = cartList[1][i]
    xCheck = 1- abs((answerX-x)/answerX)
    yCheck = 1- abs((answerY-y)/answerY)
    if xCheck and yCheck>0.99:
        print("Q %d:Pass" %i)
    else:
        print("Q %d:Fail" %i)
##something going on here needs fixing
print("Testing Cartesian to Polar Coordinates")
for i in range (0, len(polarList[0])):
    (rad, ang) = cartToPolar(cartList[0][i],cartList[1][i])
    answerRad = float(polarList[0][i])
    answerAng = float(polarList[1][i])
    radCheck = 1-float(abs((answerRad-rad)/answerRad))
    angCheck = 1-float(abs((answerAng-ang)/answerAng))
    if (radCheck and angCheck > 0.99):
        print("Q %d:Pass" %i)
    else:
        print("Q %d:Fail" %i)

print("Testing Complete")
