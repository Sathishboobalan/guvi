#holiday or not
def holiday():
    str=input()
    c=str.capitalize()
    if (c=='Sunday' or c=='Saturday'):
        print("yes")
    else:
        print("no")
try:
    holiday()
except:
    print("invalid")
