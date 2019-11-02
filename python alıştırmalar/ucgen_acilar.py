# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 22:22:33 2019

@author: HAKKI
"""

a=int(input("Birinici açıyı giriniz: "))
b=int(input("İkinci açıyı giriniz: "))
c=int(input("Üçüncü açıyı giriniz: "))

toplam=(a+b+c)
if toplam==180:
    print("Üçgen çizilebilir")
else:
    print("Üçgen çizilemez.")