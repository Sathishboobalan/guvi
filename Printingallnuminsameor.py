#printing all number in same order
n=int(input())
count=0
a=[]
temp=n
while temp>0:
    letter=temp%10
    a.append(letter)
    temp=int(temp/10)
print((a[::-1]))
