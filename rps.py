# We are building a game as - Rock, Paper, Scissors ahead of the code.
# Hit ctrl+B to hide the file explorer and make the code more visible.

import sys
import random
from enum import Enum

class RPS(Enum): # class is used to create a new user-defined class. Enum is a class in python that allows you to create enumerations, which are a set of symbolic names bound to unique constant values.
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS.ROCK)
# print(RPS.ROCK.value)

print("") 
print("Welcome to Rock, Paper, Scissors!")
print("=================================")
print("")
print("It's time to play!")
print("Enter your choice number:\n")
YourChoice = input("1 For Rock\n2 For Paper\n3 For Scissors\n\n")
print("")

Your = int(YourChoice)

if Your < 1 or Your > 3:
    sys.exit("Invalid choice! You must enter 1,2 or 3.")

ComputerChoice = random.choice("123") # random.choice() is used to select a random element from a non-empty sequence.
Computer = int(ComputerChoice)

# print(RPS(Your))
print("Your choice is: "+ str(RPS(Your)).replace('RPS.','')+ " \nComputer choice is: " + str(RPS(Computer)).replace('RPS.','')) #we explicitly mention str to convert the enum to string.
print("")

if Your == 1 and Computer == 3:
    print("You win! Rock crushes Scissors😊")
elif Your == 2 and Computer ==1:
    print("You win! Paper covers Rock😁")
elif Your == 3 and Computer ==2:
    print("You win! Scissors cuts Paper😎")
elif Your == Computer:
    print("It's a tie!🤢.")
else:
    print("You lose!🤷‍♀️")

sys.exit("\nThank you for playing!")