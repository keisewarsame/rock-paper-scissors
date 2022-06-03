import random
from ascii import rock, paper, scissors


#Write your code below this line 👇
possibles = [rock, paper, scissors]

while True:
  computer = random.randint(0, 2)
  user = int(input("Select 0 for rock, 1 for paper, or 2 for scissors or 9 to exit - "))  
  
  if user >= 3 or user < 0:
    print("Invalid input, please type 0, 1 or 2!")
  else:
    print("\YOU CHOSE \n", possibles[user])
    print("\nCOMPUTER CHOSE \n", possibles[computer])
    if user == 0 and computer == 2:
      print("YOU WIN")
    elif computer == 0 and user == 2:
      print("YOU LOSE")
    elif computer > user:
      print("YOU LOSE")
    elif user > computer:
      print("YOU WIN")
    elif user == computer:
      print("DRAW")
      
  if user >= 3 and user != 9:
    print("Invalid input, please type 0, 1 or 2!")
  elif user == 9:
    break