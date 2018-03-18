#gcd
def gcd(x,y):
    while(y):
        (x,y)=y,x%y
    return x
x=int(input())
y=int(input())
gcd(x,y)
