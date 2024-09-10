print("Finding wheather tringle is valid or not .","\n For that you need to give all three angles of tringle")
a =int(input("Enter first angle :"))
b =int(input("Enter second angle :"))
c =int(input("Enter third angle :"))
d=a+b+c
if d==180 :
    print("Tringle is valid")
else :
    print("Tringle is not valid")
