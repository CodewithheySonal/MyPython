# We are building a game as - Rock, Paper, Scissors ahead of the code.
# Hit ctrl+B to hide the file explorer and make the code more visible.


# adding Loop to play the game again and again.
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS.ROCK)
# print(RPS.ROCK.value)

playagain = True
while playagain:
 # ctrl+] to fix indentation in multiple lines.
    
    print("\n\nWelcome to Rock, Paper, Scissors!")
    print("=================================\n")
    print("It's time to play!")
    print("\nEnter your choice number:\n")
    YourChoice = input("1 For Rock\n2 For Paper\n3 For Scissors\n\n")
    

    Your = int(YourChoice)

    if Your < 1 or Your > 3:
        sys.exit("Invalid choice! You must enter 1,2 or 3.")

    ComputerChoice = random.choice("123")
    Computer = int(ComputerChoice)

    # print(RPS(Your))
    print("Your choice is: "+ str(RPS(Your)).replace('RPS.','')+ " \nComputer choice is: " + str(RPS(Computer)).replace('RPS.','')) #we explicitly mention str to convert the enum to string.
    print("")
# windows+. to open the emoji keyboard.
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

    playagain = input("\n\nDo you want to play again? \nEnter Y for Yes\nEnter Q for Quit\n\n").lower()
    if playagain == "y":
        print("\nLet's play again 😊\n\n ")
        continue
    else:
        print("\nThanks for playing!")
        playagain == False
       
sys.exit("See you next time🎗\n")