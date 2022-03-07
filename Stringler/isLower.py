# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:36:03 2022

@author: Onur BOZKURTOGLU
"""

def isLower(word):
    if (str.lower(word) == word):
        return "\'" + word + "\'" + " tamamen küçük harflerden oluşmaktadır.";
    else:
        return "\'" + word + "\'" + " tamamen küçük harflerden oluşmamaktadır.";

print(isLower("ahmet"))
print(isLower("Ahmet"))

print("*****------------******")

print(isLower("ABCD"))
print(isLower("abcd"))
