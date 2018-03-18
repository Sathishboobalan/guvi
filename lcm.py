#lcm
def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if (greater % x == 0) and (greater % y==0):
            lcm=greater
            break
        greater+=1
    return lcm
x=int(input("Enter the 1st number"))
y=int(input("enter the 2nd number"))
lcm(x,y)
