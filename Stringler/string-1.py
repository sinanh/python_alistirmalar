"""
 Girilen bir kelimenin tamamen küçük harflerden oluşup olmadığını yazan bir program yazın.

 ahmet, erzurum, ankara gibi girdiler için ekrana "girilen kelimeler küçük harflerden oluşur"
 Ahmet, erzURum, ANKARA gibi girdiler için ise ekrana "kelimede büyük harfler vardır"
"""
a = input()
if(a == a.lower()):
    print("girilen kelimeler küçük harflerden oluşur")
else:
    print("kelimede büyük harfler vardır")

