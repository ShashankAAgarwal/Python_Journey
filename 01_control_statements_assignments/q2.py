c=int(input("Enter The Cost Price :"))
s=int(input("Enter The selling Price :"))
if c == s :
    pass
elif c>s :
    loss=c-s
    print("loss in bussiness of rupees :",loss)

else :
    profit=s-c
    print("profit in bussiness of rupees :",profit)
