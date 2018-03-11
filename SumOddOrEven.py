#odd even
def add(m,n):
    sum=m+n
    if(sum%2==0):
        print("Even")
    else:
        print("odd")
m=int(input("Enter the 1st number"))
n=int(input("Enter the 2nd number"))
add(m,n)
