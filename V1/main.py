import random
from dice import *

min = 1
max = 6

roll_again = "Yes" or "yes" or "y" or "Y" or "No" or "no" or "n" or "N"

while roll_again == "Yes" or roll_again == "yes" or roll_again == "y" or roll_again == "Y":
  print("Rolling...")
  print("The result: ")
  result = random.randint(min,max)
  print (result)
  
  if result == 1:dice1()
  elif result == 2:dice2()
  elif result == 3:dice2()
  elif result == 4:dice2()
  elif result == 5:dice2()
  elif result == 6:dice2()
  
  roll_again = input("Do you want to roll the dice again? Yes/No:")
  
if roll_again == "No" or roll_again == "no" or roll_again == "n" or roll_again == "N":
  print("See you next time.")
  
  