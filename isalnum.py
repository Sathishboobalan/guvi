#contain both alphabet and num or not
try:
    string=input("Enter the string")
    falg=0
    if string.isalnum() :
        print("yes")
    else:
        print("no")
except:
    print("invalid")
