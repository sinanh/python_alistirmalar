kelime = input("Bir Kelime Giriniz")
tarih = input("Doğum Tarihinizi Giriniz")
sifre = kelime + "" + tarih[len(tarih) - 2] + tarih[len(tarih) - 1]
print("sifreniz " + sifre)