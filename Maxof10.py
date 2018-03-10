#max in 10 numbers
def ma(n):
    a=[]
    for i in range(n):
        a.append(int(input()))
        max=a[0]
    for i in a:
        if i>max:
            max=i
    print("maximum",max)
n=10
ma(n)
