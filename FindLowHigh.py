n=int(input("Enter the n value"))
a=[]
for i in range(n):
    a.append(int(input()))
max=a[0]
for i in a:
    if(i>max):
        max=i
min=a[0]
for i in a:
    if(i<min):
        min=i
print("maximum",max,"minimum",min)
