#print string cmp
def comp(str1,str2):
    if str1==str2:
        print(str1)
    elif str1>str2:
        print(str1)
    else:
        print(str2)
try:
    str1=input("Enter the string1")
    str2=input("enter the string2")
    comp(str1,str2)
except:
    print("invalid")
