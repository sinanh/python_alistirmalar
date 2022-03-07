
# coded by IBRAHIM MASMANACI


#Solution by using for loop
name = input("Please enter something to check :")
print("The original string is : " + str(name))
result = False
for i in name:
    # checking for uppercase character and flagging
    if i.isupper():
        result = True
        break
# printing result
print("Does String contain uppercase character : " + str(result))
#second = input("Please enter the input : ")
#if second.__contains__(result):



#Solution without using any loop
nameSec = input("Please enter something to check :")
if nameSec.islower():
    print("girilen kelime kücük harflerden olusur")
else :
    print("girilen kelimede büyük hafrlerde bulunuyor.")










