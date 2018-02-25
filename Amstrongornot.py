#amstrong or not
total=0
n=int(input())
temp=n
count=len(str(n))
while n!=0:
    digit=n%10
    total+=digit**count
    n //= 10
if(total==temp):
    print("yes")
else:
    print("no")
