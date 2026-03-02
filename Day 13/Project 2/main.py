#                                   PROJECT 2 - THE PERFECT GUESS

# We are going to write a program that generates a random number and asks the user to guess it.
# If the player's guess is higher than the actual number, the program displays "Lower number please".
# Similarly, if the user's guess is too low, the program prints "higher number please" When the user 
# guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
# Hint: Use the random module.

import random
num2=random.randint(1,100)
count=0
while True:
    num1 = int(input("Guess a Number: "))
    if num1<num2:
        print("Higher Number please")
        count += 1
    elif num1>num2:
        print("Lower Number please")
        count += 1
    else:
        print("Number Guessed")
        count+=1
        print("Number of Guesses to arrive at the Number is ",count)
        break