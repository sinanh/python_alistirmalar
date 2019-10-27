import math

print('Angles in Triangle Code')
print('-'*50)

angle_1 = abs(float(input('Enter the first angle value: ')))
print('-'*50)

angle_2 = abs(float(input('Enter the second angle value: ')))
print('-'*50)

angle_3 = abs(float(input('Enter the third angle value: ')))
print('-'*50)

if (angle_1 and angle_2 and angle_3 != 0) and angle_1 + angle_2 + angle_3 == 180  :
    print('triangle can be drawn')

else:
    print('triangle can not be drawn')
