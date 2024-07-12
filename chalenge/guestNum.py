from sys import exit
from random import choice
def guess_GAme():
   
      userGuest = input('Guess the number am thinking between \n1 \n2 \n3\n')                  
      user = int(userGuest)
      if user < 1 or user > 3:
       print('Guess the number am thinking between \n1 \n2 \n3')
        
       return guess_GAme()
      computerGuest = choice('123')
      computer = int(computerGuest)
      if user == computer:
        print(f'computer:{computer} and you:{user} ')
        print(f'You are correct\n {'100%'} accurate ')
      elif user * 2 == computer:    
        print(f'computer:{computer} and you:{user} ')
        
        print(f'Not bad\n {'50%'} accurate ')
      else:
        print(f'computer:{computer} and you:{user} ')
        
        print(f' Really bad\n {'10%'} accurate')
        
      again = input('play Again \nY for Yes\nQ for quit').lower()
      if again not in ['y','q']:
       return guess_GAme()
      elif again == 'y':
        return guess_GAme()

      elif again == 'q':
       return print('Bye thanks for playing')
        
print(__name__)
if(__name__ == '__main__'):
   guess_GAme()   
     