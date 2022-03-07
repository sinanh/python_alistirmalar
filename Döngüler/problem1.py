import random

def my_function(argument):
    switcher = {
        1: "taş",
        2: "kağıt",
        3: "makas",
    }
    return switcher.get(argument, "nothing")
    
rnd = random.randint(1,3)
bilgisayar = my_function(rnd)


a = ""
while(True):
    a = input("Taş Kağıt Makas?")
    a = a.lower()
    
    match a:
        case "taş":
            break
        case "kağıt":
            break
        case "makas":
            break
    


if(a == bilgisayar):
    print("beraber siz: " + a +", bilgisayar: " + bilgisayar)
elif (a == "taş" and bilgisayar == "kağıt" or  a == "kağıt" and bilgisayar == "makas"):
    print("kaybettiniz siz: " + a +", bilgisayar: " + bilgisayar)
elif(a == "taş" and bilgisayar == "makas" or a == "kağıt" and bilgisayar == "taş"):
    print("kazandınız siz: " + a +", bilgisayar: " + bilgisayar)