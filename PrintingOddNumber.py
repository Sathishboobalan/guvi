#printing near odd num
def printing():
    f=0
    n=int(input())
    k=int(input(""))
    a=[]
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        if a[i]%2!=0:
            f+=1
            if f==k:
                return a[i]
                
printing()
