# your name - CS 161
# Lab #1:  Lo - Hi Game
# Can you guess the random integer between 1 and 20 (inclusive) in 4 trys?
# Write a program that randomly chooses an integer between 1 and 20 inclusive and then gives the user 4 chances to guess the hidden number.  After each incorrect answer the computer should say that the guess was too high or too low.  If the user does not guess the number after 4 trys, the computer should say: "You are out of guesses, you lose!" and then tell the user what the hidden number actually was.

import math
import random

gameNumber = math.floor(20*random.random() +1)
# print(gameNumber) #TESTING bit to compare high and low for each guess

print('4 chances to guess between 1 - 20')

# used a random guess generator to test the code faster. Will change back to standard user input
#guess = float(math.floor(20*random.random() +1 )) # guess 1 - these statements are used to test program
guess = float(input())
if guess == gameNumber : # conditional to test success in guessing correctly
    print('You Win. the number is', gameNumber)

# the following are the series of testing conditional with nested else, if statements
# goal was to nest conditionals sans 'elif' statements
else :    

    if guess < gameNumber :
        print('your guess',guess,'is too low. 3 guesses left')
        # guess = float(math.floor(20*random.random() +1 )) used to test
        guess = float(input())
        if guess == gameNumber :
            print('you win with your guess',guess,'. the number is', gameNumber)
        
        else:
            
            if guess < gameNumber :
                print('your guess',guess,'is too low again. 2 guesses left')
                # guess = float(math.floor(20*random.random() +1 )) used to test
                guess = float(input())
                if guess == gameNumber :
                    print('You win with your guess',guess, 'finally. The number is', gameNumber)
               
                else : 
                    
                    if guess < gameNumber :
                        print('your guess',guess,'is too low again. last guess')
                        # guess = float(math.floor(20*random.random() +1 )) # used to test
                        guess = float(input())
                        if guess != gameNumber :
                            print('Your guess is',guess,'and the number is',gameNumber,'You lose')
                        else : 
                            print('you win with your guess',guess,'. the number is', gameNumber)

                    else :
                        print('your guess',guess,'is too high. last guess')
                        # guess = float(math.floor(20*random.random() +1 )) used to test
                        guess = float(input())
                        if guess == gameNumber :
                            print('you win with your guess',guess,'. the number is', gameNumber)
                        else :
                            print('Your guess is',guess,'the number is',gameNumber,'you lose')

            else :
                
                print('your guess',guess,'is too high. 2 guesses left')
                # guess = float(math.floor(20*random.random() +1 )) used to test
                guess = float(input())
                if guess == gameNumber :
                    print('you win with your guess',guess,'. the number is', gameNumber)
                else :
                    if guess < gameNumber :
                        print('your guess',guess,'is too low. last guess')
                        #guess = float(math.floor(20*random.random() +1 )) used to test
                        guess = float(input())
                        if guess == gameNumber :
                            print('you win with guess',guess,'. the number is', gameNumber)
                        else :
                            print('Your final guess is',guess,'and the number is',gameNumber,'you lose')
                    
                    else : 
                        if guess > gameNumber : 
                            print('Ok, you are too high with guess',guess,'. last guess')
                            # guess = float(math.floor(20*random.random() +1 )) used to test
                            guess = float(input())
                        if guess == gameNumber :
                            print('you win with guess',guess,'. the number is', gameNumber)
                        else :
                            if guess != gameNumber :
                                print('Your final guess is',guess,' and the number is',gameNumber,'you lose')
                    
    else : 
        
        print('your guess',guess,' is too high. 3 guesses left')
        # guess = float(math.floor(20*random.random() +1 )) used to test
        guess = float(input())
        if guess == gameNumber :
            print('you win with guess',guess,'. the number is', gameNumber)
        
        else :
            
            if guess > gameNumber :
                print('your guess',guess,'is too high again. 2 guesses left')
                # guess = float(math.floor(20*random.random() +1 )) used to test
                guess = float(input())
                if guess == gameNumber :
                    print('you win with guess',guess,'. the number is', gameNumber)
                
                else :
                    
                    if guess > gameNumber :
                        print('keep guessing too high with guess',guess,'. Last chance')
                        # guess = float(math.floor(20*random.random() +1 )) used to test
                        guess = float(input())
                        if guess != gameNumber :
                            print('Your guess is',guess,' and the number is',gameNumber,'you lose')
                        else :
                            print('you win with guess',guess,'. the number is', gameNumber)

                    else :
                        print('your guess',guess,' is too low. last chance')
                        # guess = float(math.floor(20*random.random() +1 )) used to test
                        guess = float(input())
                        if guess != gameNumber :
                            print('Your guess', guess,' and the number is',gameNumber,'you lose')
                        else :
                            print('you win with guess',guess,'. the number is', gameNumber)
            else :

                print('your guess',guess,'is too low. 2 guesses left')
                # guess = float(math.floor(20*random.random() +1 )) used to test
                guess = float(input())
                if guess == gameNumber :
                    print('you win with guess',guess,'. the number is', gameNumber)
                
                else :

                    if guess > gameNumber :
                        print('Your guess',guess,' is too high. last chance')
                        # guess = float(math.floor(20*random.random() +1 ))used to test
                        guess = float(input())
                        if guess != gameNumber :
                            print('Your guess is',guess,'and the number is',gameNumber,'you lose')
                        else :
                            print('you win with guess',guess,'. the number is', gameNumber)

                    else :
                        print('your guess',guess,' is too low. last chance')
                        # guess = float(math.floor(20*random.random() +1 )) used to test
                        guess = float(input())
                        if guess != gameNumber :
                            print('Your guess',guess,'and the number is',gameNumber,'you lose')
                        else :
                            print('you win with guess',guess,'. the number is', gameNumber)


