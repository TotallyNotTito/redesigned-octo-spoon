#binary conversion that takes any value for n and converts its binary equivalent. 

import math
import random

# n = math.floor(10*(random.random())+1) #choosing random input
print('input a value to discover the binary output')
n = float(input())

bVs = [] #variable for binary values
size = 0 #variable for keeping track of list size
# print(n,'is starting value') #inform user of what input value is
if (n == 0): #test conditionals for 0 and 1 inputs
    bVs.append(0)
if (n == 1):
    bVs.append(1)
    n = 0 
while (n >= 1/2): #while loop to add output values to list
    if (n/2 == math.floor(n/2)):
        bVs.append(0)
        n = math.floor(n/2)
    else :
        bVs.append(1)
        n = math.floor(n/2)
    size = size + 1 
# prints outputs prior to reordering binary values
# print(bVs)
# print(size,'is length of list')
# while loop to put binary outputs in correct order 
while (size > 0): 
    print(bVs[size-1],end='')
    size = size - 1

