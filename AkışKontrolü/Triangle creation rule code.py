import math
print('Triangle creation rule code')
print('-'*50)
side_1 = abs(int(input('Enter the first side value ')))
print('-'*50)
side_2 = abs(int(input('Enter the second side value ')))
print('-'*50)
side_3 = abs(int(input('Enter the third side value ')))
print('-'*50)

if side_1 - side_2 < side_3 < side_1 + side_2 and side_1 - side_3 < side_2 < side_1 + side_3 and side_2 - side_3 < side_1 < side_2 + side_3 :
    print('Complies with triangle creation rule')

elif side_1 == side_2 == side_3:
    print('Complies with triangle creation rule')

else:
    print('Does not conform to the triangle creation rule')
