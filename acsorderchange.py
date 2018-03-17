#print change
n=int(input("enter the size"))
a=[]
for i in range(n):
    a.append(int(input()))
    l=list(a)
for i in range (1,n):
    if l[i-1]>l[i]:
        print(l[i-1])
        break
