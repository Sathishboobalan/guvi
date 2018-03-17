#minimum among 10 num
def minimum(n):
    a=[]
    for i in range(n):
        a.append(int(input()))
        min=a[0]
        for i in a:
            if i<min:
                min=i
    print(min)
minimum(10)  
