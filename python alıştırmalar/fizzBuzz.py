# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:13:33 2019

@author: HAKKI
"""

#3fizz, 5buzz ve 15fizzbuzz e bölünen sayıları yaz
# Bir girdi al ve hafıza da tut
sayi=int(input("Bir sayı gir: "))

if sayi%3==0 and sayi%5==0:
    print("FizzBuzz")
elif sayi%3==0:
    print("Fizz")
elif sayi%5==0:
    print("Buzz")
else: 
    print("bolunmuyor")
