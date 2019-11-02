# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:05:19 2019

@author: HAKKI
"""

a=int(input("Birinici kenarı giriniz: "))
b=int(input("İkinci kenarı giriniz: "))
c=int(input("Üçüncü kenarı giriniz: "))
#a+b>c, a+c>b, b+c>a
if (abs(a-b)<c<abs(a+b)):
    print("Üçgen oluşur")
elif (abs(a-c)<b<abs(a+c)):
    print("Üçgen oluşur")
elif (abs(b-c)<a<abs(b+c)):
    print("Üçgen oluşur")
else:
    print("üçgen oluşmaz")
