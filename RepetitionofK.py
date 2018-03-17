#counting reptiton of k
def repeti(n):
    l=list(n)
    k=input("enter the number to check repetition")
    count=0
    for i in l:
        if i==k:
            count+=1
    print(count)
repeti(input("enter the number"))
