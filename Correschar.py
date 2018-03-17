#printing corresponding char
def place(n):
    string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string=list(string)
    print(string[n-1])
try:
    n=int(input())
    if(n>0 and n<=26):
        place(n)
    else:
        print("Error:enter value between 1 to 26")
except:
    print("invalid")
