# Monte Carlo Pi
#Throw Dart
#check if dart is or is not in circle

import random
import math

counter = 0
insideCircle = 0
outsideCircle = 0

while (counter < 1000000) :
    # throw dart
    # is dart in circle?
    xLoc = 2*random.random() - 1
    yLoc = 2*random.random() - 1
    counter = counter + 1

    if ((xLoc * xLoc) + (yLoc * yLoc) <= 1) :
        insideCircle = insideCircle + 1
    
    else :
        outsideCircle = outsideCircle + 1

print(insideCircle, 'darts in circle')
print(outsideCircle, 'darts outside circle')

print('pi is approximately', 4*insideCircle/1000000) #why 4?
