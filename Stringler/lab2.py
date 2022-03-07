def is_Lower(x):
    return x.islower()

x = input('Kelime girin: ')

if is_Lower(x):
    print('girilen kelime küçük harflerden oluşur.')
else:
    print('kelimede büyük harfler vardır.')