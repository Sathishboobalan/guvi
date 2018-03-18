#printing numbers in string
def printing_numbers():
    string=input("Enter the Sring")
    l=list(string)
    a=''
    for x in l:
        if x.isnumeric():
            a+=x
    print(a)
try:
    printing_numbers()
except:
    print("invalid")
