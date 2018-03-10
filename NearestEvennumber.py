#nearest even number <= n
def nearest_num(n):
    if(n%2==0):
        return n
    else:
        n=n-1
        if(n%2==0):
            return n
        else:
            nearest_num(n)
n=int(input("Enter the number"))
nearest_num(n)
