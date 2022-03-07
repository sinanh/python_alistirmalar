# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:40:57 2022

@author: bozku
"""
import random

player = input("Please, choose your role(for example, Rock, Paper, Scissors: ")
win = False;
random = random.randint(1, 3)
if random == 1:
    bot = "rock"
elif random == 2:
    bot = "paper"
else:
    bot = "scissors"

while(win != True):
    if (str.lower(player) == "rock" and bot == "scissors"):
        print("Player[" + player + "] won against bot[" + bot + "]")
        win = True
    elif (str.lower(player) == "paper" and bot == "rock"):
        print("Player[" + player + "] won against bot[" + bot + "]")
        win = True
    elif (str.lower(player) == "scissors" and bot == "paper"):
        print("Player[" + player + "] won against bot[" + bot + "]")
        Win = True
    elif (str.lower(player) == bot):
        print("It's draw. Player[" + player + "] - bot[" + bot + "]")
        break
    else:
        print("Player[" + player + "] lost against bot[" + bot + "]")
        break
