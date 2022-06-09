# ROCK PAPER SCISSORS
import random
while True:
  possible_options =["R", "P", "S", ]
  cpu=random.choice(possible_options)
  user_input= input("select between R , P , S : ")
  user_action=user_input.upper()
  print ("cpu:", cpu)
  print ("player:" , user_action)
  while user_action not in possible_options:
   user_input2= input ("invalid option!!! select between R , P , S : ")
   user_action=user_input2.upper()
  print ("cpu:", cpu)
  print ("player:" , user_action) 
  if user_action==cpu:
   print ("you tie!! play again")
  elif user_action=="R":
    if cpu =="P":
      print ("you lose!!")
    if cpu=="S":
      print ("you win!!")
    exit()
  elif user_action=="P":
    if cpu =="S":
      print ("you lose!!")
    if cpu=="R":
      print ("you win!!")
    exit()
  elif user_action=="S":
    if cpu =="R":
      print ("you lose!!")
    if cpu=="P":
      print ("you win!!")
    exit()
      

