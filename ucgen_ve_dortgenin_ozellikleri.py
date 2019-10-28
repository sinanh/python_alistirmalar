from math import sqrt

sekil = input('Hangi şekli yaptırmak istersiniz: ').lower()

if sekil == 'üçgen':
    u_islem = input('hangi işlemi yaptırmak istersiniz: ').lower()

    if u_islem == 'kenar':
        uk_1 = abs(int(input('Bir kenar giriniz: ')))
        uk_2 = abs(int(input('Bir kenar giriniz: ')))
        uk_3 = abs(int(input('Bir kenar giriniz: ')))
        uk_acı = abs(int(input('Bir açı giriniz: ')))
        if abs((uk_1 - uk_2) < uk_3 < (uk_1 + uk_2) and (uk_1 - uk_3) < uk_2 < (uk_1 + uk_3) and (uk_2 - uk_3) < uk_1 < (uk_2 + uk_3)  ):
            print('Girilen kenarlar bir üçgen oluşturabilir.') 

            if uk_1 == uk_2 == uk_3:
                print('Eşkenar üçgen')
                alan = uk_1**2*sqrt(3)/4
                cevre = uk_1 + uk_2 + uk_3 
                print(f'Eşkenar üçgenin alanı {alan} çevresi ise {cevre} dir ')

            elif uk_1 == uk_2 != uk_3 or uk_1 == uk_3 != uk_2 or uk_2 == uk_3 != uk_1:
                print('İkizkenar üçgen')
                a = max(uk_1,uk_2,uk_3)
                b = sqrt((a**2/2) / min(uk_1,uk_2,uk_3)) 
                alan = min(uk_1,uk_2,uk_3)*b/2
                cevre = uk_1 + uk_2 + uk_3
                print(f'İkizkenar üçgenin alanı {alan} çevresi ise {cevre}')
            
            elif uk_acı == 90:
                print('Dik üçgen')
                a = max(uk_1,uk_2,uk_3)
                kenarortay=a/2
                g = [uk_1, uk_2, uk_3]
                c = sorted(g)
                b = c[0]*c[1] 
                alan = b/2
                cevre = uk_1 + uk_2 + uk_3
                print(f'Dik üçgeninizin kenarortayı {kenarortay} alanı {alan} çevresi ise {cevre} dir.')

            else:
                print('Çeşitkenar üçgen')
                s = (uk_1 + uk_2 + uk_3)/2
                alan = sqrt(s*(s-uk_1)*(s-uk_2)*(s-uk_3))
                cevre = uk_1 + uk_2 + uk_3
                print(f'Çeşitkenar üçgenin alanı {alan} çevresi ise {cevre}')

        else:
            print('Girilen kenarlar bir üçgen oluşturamaz.')
            
    elif u_islem == 'açı':
        ua_1 = int(input('Bir açı değeri giriniz: '))
        ua_2 = int(input('Bir açı değeri giriniz: '))
        ua_3 = int(input('Bir açı değeri giriniz: '))
        
        if (ua_1 and ua_2 and ua_3 != 0) and ua_1 + ua_2 + ua_3 == 180:
            print('Bir üçgen oluşturabilir.')
             
            if ua_3 == 90 or ua_2 == 90 or ua_1 == 90:
                print('Dik üçgen')
            
            elif (ua_1 or ua_2 or ua_3) > 90:
                print('Geniş açılı üçgen')
            
            elif ua_1 and ua_2 and ua_3 < 90 :
                print('Dar açılı üçgen')
            

      
        else:
            print('Bir üçgen oluşturamaz.')
                
elif sekil == 'dortgen':
    dhs=input('kenar mı açı mı kullanmak istersiniz: ').lower()
    
    if dhs == 'kenar':
        dkk_1 = int(input('Bir kenar giriniz: '))   
        dkk_2 = int(input('Bir kenar giriniz: '))   
        dkk_3 = int(input('Bir kenar giriniz: '))   
        dkk_4 = int(input('Bir kenar giriniz: '))
        
        if dkk_1 == dkk_2 == dkk_3 == dkk_4:
            print('Şekliniz karedir')
            cevre = dkk_1*4
            alan = dkk_1**2
            print(f'Karenin çevresi {cevre} alanı {alan} ')
        
        elif (dkk_1 == dkk_2 and dkk_3 == dkk_4) or (dkk_1 == dkk_3 and dkk_2 == dkk_4) or (dkk_3 == dkk_2 and dkk_1 == dkk_4):
            print('Şekliniz Dikdörtgendir')
            alan= max(dkk_1, dkk_2, dkk_3, dkk_4)*min(dkk_1, dkk_2, dkk_3, dkk_4)
            cevre = dkk_1 + dkk_2 + dkk_3 +dkk_4
            print(f'alanınız {alan} çevreniz ise {cevre}')
        
        else:
            print('Şekliniz dörtgendir.')
    
    elif dhs == 'açı':
        dka_1 = int(input('Bir açı giriniz: '))        
        dka_2 = int(input('Bir açı giriniz: '))        
        dka_3 = int(input('Bir açı giriniz: '))        
        dka_4 = int(input('Bir açı giriniz: '))        
        
        if (dka_1 + dka_2 + dka_3 + dka_4 == 180):
            print('Açılar bir Dörtgen belirtir.')
        
            if dka_1 == dka_2 == dka_3 == dka_4:
                print('Şekliniz karedir.')
            
            elif (dka_1 == dka_2 and dka_3 == dka_4) or (dka_1 == dka_3 and dka_2 == dka_4) or (dka_2 == dka_3 and dka_1 == dka_4):
                print('Şekliniz dikdörtgendir.')

            else:
                print('Şekliniz dörtgendir')

        else:
            print('Açılar bir Dörtgen belirtmez.')        

else:
    print('Tanımlanamayan bir komut girdiniz.')





# MUSTAFA YILDIRIM (github.com/mustafayildirim93) ve ÖMER FARUK TOPALOĞLUNUN (github.com/oftopaloglu) KATKILARIYLA YAPILMIŞTIR.