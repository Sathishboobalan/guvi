#printing factors
def fact(n):
    a=[]
    flag=1
    for i in range(1,n+1):
        if n%i==0:
            flag=0
        else:
            flag=1
        if(flag==0):
            a.append(i)
    print(a)
fact(int(input()))
