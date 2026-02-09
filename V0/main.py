import random
from dice import *

min = 1
max = 6

roll_again = "yes" or "y" or "no" or "n"

while roll_again == "yes" or roll_again == "y":
  print ("Rolling the dice...")
  print ("The result is....")
  result = random.randint(min, max)
  print (result)

  if result == 1:
    dice1()
  elif result == 2:
    dice2()
  elif result == 3:
    dice3()
  elif result == 4:
    dice4()
  elif result == 5:
    dice5()
  elif result == 6:
    dice6()
    
  roll_again = input("Do you want to roll the dice again? Type yes or no to choose:)" )

if roll_again == "no" or roll_again == "n":
  print ("Ok, see you next time!")
  
  
