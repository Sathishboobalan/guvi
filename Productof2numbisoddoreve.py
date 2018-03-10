#product of 2 num is odd or even
def odd_even(m,n):
    product=m*n
    if(product%2==0):
        print("Even")
    else:
        print("odd")
m=int(input("Enter the 1st number"))
n=int(input("Enter the 2nd number"))
odd_even(m,n)
