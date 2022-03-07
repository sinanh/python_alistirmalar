import sys

def findUpper(s):
    if s.isupper():
        return True
    return False

if __name__ == '__main__':
    print("enter city name: ", sys.argv[0])
    if findUpper(str(sys.argv)):
        print('girilen kelimelerde buyuk harftir')
    else:
        print('girilen kelimelerde kucuk harftir')
