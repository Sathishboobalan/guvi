#fibonacci
n=int(input("Enter the number"))
i=0
fib0=0
fib1=1
while i<n:
    if i<=1:
        fibnext=i
    else:
        fibnext=fib0+fib1
        fib0=fib1
        fib1=fibnext
    i=i+1
    print(fibnext)
