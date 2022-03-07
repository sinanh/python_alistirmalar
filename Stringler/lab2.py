def func(x):
    if x.islower():
        return True
    else:
        return False

print('Kelime girin: ', end="")
x = input()

if(func(x)):
    print('girilen kelime küçük harflerden oluşur.')
else:
    print('kelimede büyük harfler vardır.')