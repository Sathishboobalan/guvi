#check the num bet 2 num or not
def chec(n):
    flag=0
    begin=int(input("Enter the starting number"))
    end=int(input("Enter the ending number"))
    for i in range(begin,end):
        if (n>=begin and n<=end):
            flag=1
    if flag==1:
        print("yes")
    else:
        print("no")
    
n=int(input("Enter the num to check"))
chec(n)
