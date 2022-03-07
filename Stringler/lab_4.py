import sys

def findUpper(s):
    for i in range(len(s)):
        if s[i].isupper():
            return True
    return False

if __name__ == '__main__':
    print("enter city name: ", sys.argv[0])
    if findUpper(str(sys.argv)):
        print('girilen kelimelerde buyuk harftir')
    else:
        print('girilen kelimelerde kucuk harftir')
