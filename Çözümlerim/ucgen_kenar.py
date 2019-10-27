#k = kenar. Ör: k2 = 2. kenar 

k1 = abs(float(input("İlk kenarın uzunluğunu giriniz.")))
k2 = abs(float(input("İkinci kenarın uzunluğunu giriniz.")))
k3 = abs(float(input("Üçüncü kenarın uzunluğunu giriniz.")))

if abs((k1 - k2) < k3 < (k1 + k2) and (k1 - k3) < k2 < (k1 + k3) and (k2 - k3) < k1 < (k2 + k3)):
    print("Üçgen oluşturur.")

else:
    print("Üçgen oluşturmaz.")