#odd and even char string
def ordering():
    s=input()
    l=list(s)
    (e,o)=('','')
    for i in range(len(l)):
        if i%2==0:
            e+=l[i]
        else:
            o+=l[i]
    print(e,o)
ordering()
