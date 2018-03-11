#composite or not
def compo_or_not(n):
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
    if flag==0:
        print("Yes")
    else:
        print("no")
n=int(input("Enter the number to check composite"))
compo_or_not(n)
