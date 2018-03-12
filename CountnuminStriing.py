#Count numbers in string
try:
    string=input("Enter the string")
    count=0
    l=list(string)
    for i in l:
        if i.isnumeric() == True:
            count=count+1
    print(count)
except:
    print("invalid")
