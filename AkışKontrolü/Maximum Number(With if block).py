print("MAXİMUM NUMBER CODE")

value_1 = int(input('Enter the first number value: '))
value_2 = int(input('Enter the second number value: '))
value_3 = int(input('Enter the third number value: '))

if value_1 == value_2 == value_3:
    print('The number are equal')
     
elif value_1 > value_2 > value_3:
    print(f'Maximum number = {value_1}')

elif value_2 > value_3 > value_1:
    print(f'Maximum number = {value_2}')

elif value_3 > value_2 > value_1:
    print(f'Maximum number = {value_3}')
