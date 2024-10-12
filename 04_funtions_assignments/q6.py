n=int(input("enter "))
add=0
for i in range(1,n):
  if n%i==0:
    add+=i
if add==n:
  print("true")
else:
  print("false")