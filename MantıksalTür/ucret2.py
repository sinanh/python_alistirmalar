#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 15:16:33 2019

@author: hakki
"""

yas = int(input("yaşınızı girin"))

if yas < 18:
    print("2 lira")
elif yas > 18 and yas < 65:
    print("3 lira")
else:
    print("ücretsiz")