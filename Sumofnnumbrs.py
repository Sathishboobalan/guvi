#sum of all digit
n=int(input("Enter the number"))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=int(n/10)
print(sum)
