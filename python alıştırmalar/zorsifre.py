# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 23:34:41 2019

@author: HAKKI
"""

sifre=input("Büyük ve küçük harflerden oluşan bir şife giriniz: ")
if sifre.islower() or sifre.isupper():
    print("En az bir büyük yada küçük harf kullanınız!")
else:
    sifretekrar=input("Şifreyi tekrar giriniz: ")
    if sifre==sifretekrar:
        print("Şifre onaylandı!")
