#replacing * in middle
string=input("Enter the String")
length=len(string)
list1=list(string)
middle=length//2
list1[middle]='*'
ans=''
for x in list1:
    ans=ans+x
print(ans)
