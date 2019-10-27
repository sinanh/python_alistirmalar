#a = açı. Örn: a3 = 3. kenar

a1 = abs(float(input("İlk açıyı giriniz.")))
a2 = abs(float(input("İkinci açıyı giriniz.")))
a3 = abs(float(input("Üçüncü açıyı giriniz.")))


if (a1 and a2 and a3 != 0) and a1 + a2 + a3 == 180:
    print("Üçgen oluşturur.")

else:
    print("Üçgen oluşturmaz.")