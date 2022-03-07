kenar1 = int(input("ilk kenarı Giriniz"))
kenar2 = int(input("ikinci kenarı Giriniz"))
kenar3 = int(input("üçüncü kenarı Giriniz"))


if((kenar1 + kenar2 >kenar3) and kenar1 + (kenar3 >kenar2) and (kenar2 + kenar3 >kenar1)):
    print("bu bir üçgendir")
else:
    print("bu bir üçgen değildir.")