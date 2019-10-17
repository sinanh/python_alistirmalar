#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:29:02 2019

@author: sinan
"""

SIFRE = 'şafak'

girilen_sifre = input('şifrenizi girin')
esit_mi = girilen_sifre == SIFRE

print('girilen gerçek şifreye eşit mi: ', esit_mi)
