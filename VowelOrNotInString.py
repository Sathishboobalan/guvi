#vowel or not
def vowel():
    flag=0
    inp=input("Enter the string")
    lisp=list(inp)
    for i in lisp:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            flag+=1
    if(flag==(len(inp))):
        print("yes")
    else:
        print("no")
        
vowel()
