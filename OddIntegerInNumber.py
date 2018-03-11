#printing odd digits in the number
def series():
    a=[]
    n=int(input())
    while n!=0:
        temp=n%10
        if(temp%2!=0):
            a.append(temp)
        n=int(n/10)
    for i in a:
        print(i)
series()
