taskagıtmakas = ['tas','kagıt','makas']        
import random
tas = taskagıtmakas[0]
kagıt = taskagıtmakas[1]
makas = taskagıtmakas[2]
sayac = 1
kazanılan = 0
kaybedilen = 0
berabere = 0
tur =int(input('kaç tur oyun oynamak istersiniz'))
while sayac <= tur:
    
    gir = input('taş mı? kağıt mı? makas mı?')

    a = random.choice(taskagıtmakas)
    print(f'bilgisayar {a} seçti')
    if gir == 'kagıt':
        sayac += 1
        if kagıt == a:
            print('berabere')
            berabere +=1
        elif tas == a:
            print('kazandınız')
            kazanılan +=1
        elif makas == a:
            print('kaybettiniz')
            kaybedilen += 1
    elif gir == 'tas':
        sayac += 1
        if kagıt == a:
            print('kaybettiniz')
            kaybedilen += 1
        elif tas == a:
            print('berabere')
            berabere += 1
        elif makas == a:
            print('kazandınız')
            kazanılan += 1
    elif gir == 'makas':
        sayac += 1
        if kagıt == a:
            print('kazandınız')
            kazanılan += 1
        elif tas == a:
            print('kaybettiniz')
            kaybedilen +=1
        elif makas == a:
            print('berabere')
            berabere += 1


if kazanılan > kaybedilen:
    print(f'Oyunu kazanılan: {kazanılan}-kaybedilen: {kaybedilen} şeklinde kazandınız.')
elif kazanılan < kaybedilen:
    print(f'Oyunu kazanılan: {kazanılan}-kaybedilen: {kaybedilen} şeklinde kaybettiniz.')
elif kazanılan == kaybedilen:
    print('Berabere kaldınız')
