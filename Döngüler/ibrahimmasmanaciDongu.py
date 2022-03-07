import random

#Coded by ibrahim Masmanacı
#Game iterates unless there is a winner , otherwise it loops.

gameLoops = True

while (gameLoops):
    userSelection = input("Birini sec ! ->   (1 = Taş) , (2 = Kağıt) , (3 = Makas ) = ")
    i = (random.randint(1, 3))
    pcSelection = ""

    if i == 1:
        pcSelection = "Taş"
        if (userSelection == "1" or "Taş"):
            print("Pc secimi = " + pcSelection + ", Senin secimin = " + "Taş")
            print("berabere!")
            gameLoops = True
        elif (userSelection =="2" or "Kağıt"):
            print("Pc secimi = " + pcSelection + ", Senin secimin = " + "Kağıt")
            print("Kazandın!")
            gameLoops= False
        elif (userSelection =="3" or "Makas"):
            print("Pc secimi = " + pcSelection + ", Senin secimin = " + "Makas")
            print("Kaybettin!")
            gameLoops = False

    elif i== 2 :
        pcSelection = "Kağıt"
        if (userSelection == "1" or "Taş"):
            print("Pc secimi = " + pcSelection + ", Senin secimin = " + "Taş")
            print("kaybettin!")
            gameLoops = False

        elif (userSelection =="2" or "Kağıt"):
            print("Pc secimi = " + pcSelection + ", Senin secimin = " + "Kağıt")
            print("Berabere!")
            gameLoops = True

        elif (userSelection  == "3" or "Makas"):
            print("Pc secimi = " + pcSelection + ", Senin secimin = " + "Makas")
            print("Kaybettin!")
            gameLoops = False

    elif i==3 :
        pcSelection = "Makas"
        if (userSelection == "1" or "Taş"):
            print("Pc secimi = " + pcSelection + ", Senin secimin = " + "Taş")
            print("kazandın!")
            gameLoops = False

        elif (userSelection =="2" or "Kağıt"):
            print("Pc secimi = " + pcSelection + ", Senin secimin = " + "Kağıt")
            print("kaybettin!")
            gameLoops = False

        elif (userSelection == "3" or "Makas"):
            print("Pc secimi = " + pcSelection + ", Senin secimin = " + "Makas")
            print("berabere!")
            gameLoops = True

    else:
        print("Geçerli birsey seçemediniz..")

request = input("Tekrar oynamak istiyorsanız (+)'ya oynamak istemiyorsanız (-)'ye tıklayınız")
if(request == "+") :
    gameLoops = True
else:
    gameLoops = False



