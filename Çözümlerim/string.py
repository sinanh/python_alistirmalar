kelime = input("Bir kelime giriniz.")

if kelime.islower():
    print("Harfler küçüktür.")

elif kelime.isupper():
    print("Harfler büyüktür.")

else:
    print("Hem küçük hem büyük harfler vardır veya girilen değerlerin tamamı alfabe dışı karakterlerdir.")