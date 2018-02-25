#prime or not
n=int(input("Enter the number"))
flag=1
for i in range(2,int(n/2)):
    if n%i==0:
        flag=0
if flag==0:
    print("No")
else:
    print("Yes")
