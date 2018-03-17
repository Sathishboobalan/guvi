#printing corresponding char
string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string=list(string)
n=int(input())
if n>0 and n<=26:
    print(string[n-1])
else:
    print("Error:Enter value between 1 to 26")
