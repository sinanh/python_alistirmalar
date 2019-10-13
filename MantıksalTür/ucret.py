#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 10:55:28 2019

@author: sinan
"""

yas = input('yaşınızı girin')

if yas < 18:
    print('2 lira')

elif yas < 65:
    print('3 lira')

else: 
    print('ücretsiz')

print('program bitti')