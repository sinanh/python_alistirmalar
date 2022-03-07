import random

l = ['rock','paper','scissors']
computer = random.randint(1,4)

print("rock: 1, paper: 2, scissors: 3\nwhat is your choice(1/2/3) : ")
choice = int(input())
print("you have chosen :" + l[choice-1])

if(computer == choice):
    print("draw")
if(choice == 1):
    if(computer == 2):
        print("computer chosed paper. You lost!")
    if(computer == 3):
        print("computer chosed scissors. You win!")
if(choice == 2):
    if(computer == 3):
        print("computer chosed scissors. You lost!")
    if(computer == 1):
        print("computer chosed paper. You win!")
if(choice == 3):
    if(computer == 1):
        print("computer chosed rock. You lost!")
    if(computer == 3):
        print("computer chosed paper. You win!")

