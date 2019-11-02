# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:50:48 2019

@author: HAKKI
"""

yas = int(input("Yaşınızı Giriniz: "))
if yas < 18:
    print("2 Lira")
elif yas >18 and yas <65 :
    print ("3 lira")
else:
    print("Ücretsiz")