#string count lines
x=(input("Enter the String"))
count=1
for i in x:
    if(str(i)=='.'):
        count+=1
print(count)
