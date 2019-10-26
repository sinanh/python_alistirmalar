#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tip = input("Lütfen istediğiniz şekili giriniz(1-Dikdörtgen ,2-Kare)").strip()
if tip=="2":
    a=int(input("1. kenar"))
    b=int(input("2. kenar"))
    c=int(input("3. kenar"))
    d=int(input("4. kenar"))
    
    if a==b==c==d:
        print("Bu bir karedir")
    else:
        print("Bu bir kare değildir")
    
        
elif tip=="1":
    a=int(input("1. kenar"))
    b=int(input("2. kenar"))
    c=int(input("3. kenar"))
    d=int(input("4. kenar"))
    if (a == b and d==c) or (a==c and b==d) or (a==d and b==c):
        print("Bu bir dikdörtgendir")
    else:
        print ("Bu bir dikdörtgen değildir.")
    
else:
    print("Bu bir dikdörtgen değildir.")
    
        
