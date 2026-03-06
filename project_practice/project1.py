# snake water gun
import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])

your_choice = input("enter your choice: ")
youdict = {"snake" : 1 , "water" : -1 , "gun": 0}
reverse_dict = {1 :"snake" ,-1 :  "water" , 0: "gun"}
you = youdict[your_choice]

print(f"You choose {reverse_dict[you]}\nComputer choose {reverse_dict[computer]}")

if computer == you :
    print("its a draw")
else:
   if (computer == -1 and you == 1):
    print("You Win !!!")

   elif (computer == -1 and you == 0):
    print("You lose")

   elif (computer == 1 and you == -1):
    print("You lose")

   elif (computer == 1 and you == 0):
    print("You Win !!!")

   elif (computer == 0 and you == -1):
    print("You Win !!!")

   elif (computer == 0 and you == 1):
    print("You lose")

   else:
    print("something went wrong!!")
