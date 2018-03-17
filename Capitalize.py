#capilalize first wrd
def capitalize():
    s=input()
    l=s.split()
    st=''
    for i in l:
        st+=i.title()+' '
    print(st)
capitalize()
