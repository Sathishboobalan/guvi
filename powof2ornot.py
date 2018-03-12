#power of 2 or not
def pow_of_two(n):
    n=int(n/2)
    if (n==2):
        print("yes")
    else:
        if n>2:
            pow_of_two(n)
        else:
            print("no")
try:
    n=int(input("Enter the number"))
    pow_of_two(n)
except:
    print("invalid")
