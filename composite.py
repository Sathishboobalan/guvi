#composite or not
def composite(n):
    flag=1
    for i in range(2,n):
        if(n%i)==0:
            flag=0
    if(flag==1):
        print("no")
    else:
        print("yes")
composite(int(input()))
            
