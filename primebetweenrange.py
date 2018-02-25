#prime within range
m=int(input("Enter the Start range"))
n=int(input("Enter the end range"))

for n in range(m,n+1):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=0
            break
        else:
            flag=1
    if flag==1: 
        print(n)
