n=int(input("Enter the Number"))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if(temp==rev):
    print("Yes")
else:
    print("No")
