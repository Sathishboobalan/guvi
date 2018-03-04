#printing element with its index
a=[]
n=int(input("Enter the size"))
for i in range(n):
    a.append(int(input()))
count=0
for i in a:
    print("position:",count,"value",i)
    count+=1
