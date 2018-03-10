#string count  space
x=(input("Enter the String"))
count=0
for i in x:
    if(str(i)==' '):
        count+=1
print(count)
