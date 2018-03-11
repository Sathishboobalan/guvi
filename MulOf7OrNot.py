#multiple of 7 or no
def multi7():
    n=int(input("Enter the number"))
    if(n%7==0):
        print("yes")
    else:
        print("no")
    
        
try:
    multi7()
except:
    print("invalid")
