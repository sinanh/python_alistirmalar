
sayi1 = int(input("ilk sayı Giriniz"))
sayi2 = int(input("ikinci sayı Giriniz"))
sayi3 = int(input("üçüncü sayı Giriniz"))

max = 0
if(sayi1 > sayi2):
    max = sayi1
else:
    max = sayi2

if(sayi3 > max):
    max = sayi3

print("En büyük ",max, "dır")

result = max(sayi1,sayi2,sayi3)
print("The maximum number is:", result)