import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
# this are the ways of getting data out of enum
    #rock paper scissoces = rps no forget
#print(RPS(1))
#print(RPS.ROCK)
#print(RPS.ROCK.value)
#sys.exit('')

print("")

playerChoice = input("Enter...\n 1 for Rock,\n2 for paper, or\n3 for scissors:\n\n")

player = int(playerChoice)
if player < 1 or player > 3:
    # sys.exit is use for exiting the program to prevent contue it also return message
    sys.exit("you must enter 1,2, or 3. ")
computerChoice = random.choice("123")

computer = int(computerChoice)

print("")
# replae acept two value what to chang and to new valu
print("you chose " + str(RPS(player)).replace('RPS.','') + ".")
print("python chose " + str(RPS(computer)).replace('RPS.','') + ".")
print('testing', RPS(player))
print("")

if player == 1 and computer == 3:
    print("You win!😁")
elif player == 2 and computer == 1:
    print("You win!😁")
elif player == 3 and computer == 2:
    print("You win!😁")
elif player == computer:
    print("Tie game!👀")
else:
    print("computer wins!🤷‍♀️")
