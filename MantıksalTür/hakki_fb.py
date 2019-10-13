#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 15:39:09 2019

@author: hakki
"""


#Bir sayı gir ve inte çevir
sayi=int(input("Lütfen Bir sayı giriniz"))
#sayinin 3ile bölümünden kalan sıfır ise Fizz yazsın
if sayi%3==0 and sayi%5==0:
    print("FizzBuzz")
elif sayi%3==0:
    print("Fizz")
elif sayi%5==0:
    print("Buzz")
else:
    print('ne 3e ne 5e bolunur')
