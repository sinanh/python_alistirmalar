import math


şekil = input("Üçgen mi Dörtgen mi?").lower()

if (şekil == "dörtgen") :
    print("Dört tane kenar girin.")
    a = float(input("İlk kenarı gir."))
    b = float(input("İkinci kenarı gir."))
    c = float(input("Üçüncü kenarı gir."))
    d = float(input("Dördüncü kenarı gir."))

    if a == b and a == c and a == d :
        print("Kare")
    elif a == b and c ==d or a == c and b == d or a == d and b == c:
        print("Dikdörtgen")
    else:
        print("Dörtgen")

elif (şekil == "üçgen"):
    print("Üç tane kenar girin.")
    a = abs(float(input("İlk kenarı gir.")))
    b = abs(float(input("İkinci kenarı gir.")))
    c = abs(float(input("Üçüncü kenarı gir.")))

    if abs((a-b)< c < (a+b) and (a-c) < b < (a+c) and (b-c) < a < (b+c)):
        if a == b and a == c:
            print("Eşkenar üçgen.")
        elif a == b and a != c or a == c and a != b or b == c and b != a:
            print("İkizkenar üçgen")
        else:
            print("Çeşitkenar üçgen.")
    else:
        print("Üçgen belirtmiyor.")

else:
    print("Şekil tanımlanamadı.")
