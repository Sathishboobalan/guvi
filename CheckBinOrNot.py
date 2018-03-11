#check it bin num or not
def bin_or_not():
    b=input()
    flag=0
    for i in b:
        if((i=='0') or (i=='1')):
            flag+=1
    if(flag==(len(b))):
        print("yes")
    else:
        print("no")
bin_or_not()
