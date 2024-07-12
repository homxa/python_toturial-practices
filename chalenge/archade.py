from ..adRockL8 import rps_Game


import sys
import guestNum 
#import  adRockL8
#rps_Game = adRockL8.rps_Game
gess_Game = guestNum.guess_GAme
def arcade():
  player_input = input('Wellcome to Arcade press\n 1 for Guess_Game\n2 for RPS Game    ')
  if player_input not in ['1','2','3']:
    return arcade()
  
   
  player = int(player_input)
  if player < 1 or player > 3:
    return arcade()
  
  if player == 1:
    return  gess_Game()
  elif player == 2:
    return rps_Game()
arcade()  
  