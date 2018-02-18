arr=[]
count=0
add=0
N=int(input("n value"))
K=int(input("k value"))
for i in range(1,N+1):
    arr.append(i)
for i in arr:
    count=count+1
    if count<=K:
        add=add+i

print(add)
