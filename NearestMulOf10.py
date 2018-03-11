#printing nearest multiple of 10
def count1(n):
    temp=n
    temp=n-(n%10)
    temp1=temp+10
    print(temp1)
n=int(input("Enter the number"))
count1(n)
