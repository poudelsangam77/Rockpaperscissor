import sys
import random 

while True:
 print("Choose between these three:\n1).Scissor\n2).Paper\n3).Rock")
 dicti={1: "Scissor", 2: "Paper", 3: "Rock"}

 playerchoice=input("Enter Your Choice:\n")

 player=int(playerchoice)

 if(player < 1 or player>3):
  sys.exit("please choose the correct option.")

 computerchoice=random.choice("123")
 computer=int(computerchoice)
 if(player==1):
  print(f"Your choice:{dicti[1]}")
 elif(player==2):
  print(f"Your choice:{dicti[2]}")
 else:
  print(f"Your choice:{dicti[3]}")

 if(computer==1):
  print(f"Computer's choice:{dicti[1]}")
 elif(computer==2):
  (f"Computer's choice:{dicti[2]}")
 else:
  print(f"computer's choice:{dicti[3]}")

 #situation of the win by the user 

 if(player==1 and computer==2):
   print("Congratulations 🏆🎉\nYou win")
 elif(player==2 and computer==3):
   print("Congratulations 🏆🎉\n You win")
 elif(player==3 and computer==1):
   print("Congratulations  🏆🎉\n You win")

 elif(player==computer):
   print("Game is Draw 🤝")

 else:
  print("Computer Wins!🤖👑")
  
 playagain=input("Play again?\nChoose Y for again and any key for No:")
 if playagain.lower()=="y":
   continue
 else:
   print("\nThanks you for playing the game")
   break


 






