#product of digits
def prod_digis():
    prod=1
    n=int(input("Enter the numbers"))
    while n!=0:
        digits=n%10
        prod*=digits
        n//=10
    print(prod)
prod_digis()
        
