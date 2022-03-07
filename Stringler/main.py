import sys


def findlower(s):

    if s.islower():
        return True


stringAdi = input("-> String Adını Girin: ")

if findlower(stringAdi):
    print('girilen kelimelerde kucuk harftir')
else:
    print('girilen kelimelerde buyuk harftir')
