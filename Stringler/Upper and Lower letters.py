word = input('Enter a word: ')

if not word.islower():
    print('The word consists of upper letters')

elif not word.isupper():
    print('The word consists of lower letters')