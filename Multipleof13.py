#Check it is mul of 13
def mul13(n):
    if n%13==0:
        print("yes")
    else:
        n=n-13
        if n>13:
            mul13(n)
        else:
            print("no")
n=int(input())
mul13(n)
