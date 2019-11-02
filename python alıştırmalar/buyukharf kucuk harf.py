# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 22:41:46 2019

@author: HAKKI
"""
kelime=input("Bir kelime giriniz: ")
if kelime.islower() :
    print("Girilen kelimeler küçük harflerden oluşur")
elif kelime.isupper():
     print("Girilen kelimeler büyük harflerden oluşur")
else :
    print("Kelime büyük ve küçük harflerden oluşur.") 