import random
from enum import Enum
import sys

class RPS(Enum):
  Rock = 1
  Papper = 2
  Scissoce = 3
playAgain = True
def rps_Game():
  playerChoice = input('Enter...\n 1 for Rock,\n2 for paper, or\n3 for scissors:\n\n')
  player = int(playerChoice)
  if player < 1 or player > 3:
   return rps_Game()
  computerChoice = random.choice('123')  
  computer = int(computerChoice)
  print(' ')

  print('You pick ' + str(RPS(player)).replace('RPS.',' '))
  print('Computer pick ' + str(RPS(player)).replace('RPS.',' '))

  if player == 1 and computer == 3:
    print('You win🎉')
  elif player == 2 and computer == 1:
    print('You win🎉')
  elif player == 3 and computer ==  2:
    print('You win🎉')
  elif player == computer:
    print('Tie Game')

  else:
    print('Computer wins🐱‍👤')
  choose = input('playAgain \nY for Yes\nQ for Quit\n\n').lower()
  if choose == 'y':
   return rps_Game()
  else:
   return print('bye thanks for playing')
 
rps_Game()
