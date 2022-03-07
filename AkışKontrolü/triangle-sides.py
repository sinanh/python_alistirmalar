a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))

if(a+b>c and b+c>a and a+c>b):
    print("It is possible to draw a triangle")
else:
    print("You can not draw a triangle")
    
