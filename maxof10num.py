#max in 10 numbers
a=[]
for i in range(10):
    a.append(int(input()))
max=a[0]
for i in a:
    if i>max:
        max=i
print("maximum",max)
