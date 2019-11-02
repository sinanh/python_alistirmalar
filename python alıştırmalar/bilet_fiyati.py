# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:17:03 2019

@author: HAKKI
"""

vasita=input("Vasıta giriniz: ")
if vasita=="otobüs":
    print("90 lira")
elif vasita=="uçak" or "tren":
    sinif=input("Sınıfı giriniz: ")
    if vasita == "uçak":
        if sinif=="ekonomi":
            print("200 lira")
        elif sinif=="business":
            print ("300 lira")
    elif vasita=="tren":
        if sinif == "1":
            print("80")
        elif sinif== "2":
            print("120")
else:
    print("Geçersiz Taşıt...")