#prime or not
def prime_or_not(n):
    flag=1
    for i in range(2,int(n/2)):
        if n%i==0:
            flag=0
    if flag==1:
        print("Yes")
    else:
        print("no")
n=int(input("Enter the number to check prime or not"))
prime_or_not(n)
