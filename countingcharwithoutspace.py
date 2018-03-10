#string count without space
x=(input("Enter the String"))
count=0
for i in x:
    if(str(i)==' '):
        count=count
    else:
        count+=1
print(count)
