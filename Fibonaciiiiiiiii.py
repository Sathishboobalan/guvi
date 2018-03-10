#fibonacci
def fibo(n):
    
    i=1
    fib0=0
    fib1=1
    while i<n+1:
        if i<=1:
            fibnext=i
        else:
            fibnext=fib0+fib1
            fib0=fib1
            fib1=fibnext
        i=i+1
        print(fibnext)
n=int(input("Enter the number"))
fibo(n)
