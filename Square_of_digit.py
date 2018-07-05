#sum of Squ of Digits
def sumofdig(n):
    sum=0
    while n>0:
        digit=n%10
        square=digit*digit
        sum+=square
        n=int(n/10)
    print(sum)
try:
    n=int(input())
    sumofdig(n)
except:
    print("invalid")
