#time difference
hr1=int(input("enter the hr of 1st time"))
min1=int(input("Enter the minutes of 1st time"))
hr2=int(input("enter the hr of 2nd time"))
min2=int(input("Enter the minutes of 2nd time"))
temp1=(hr1*60)+min1
temp2=(hr2*60)+min2
if temp1>temp2:
    time=temp1-temp2
else:
    time=temp2-temp1
count=0
minites=time
while time>=60:
        time=time-60
        count+=1
temp=minites-(count*60)
print("hrs:",count,"minutes:",temp)
