#Print Time in Hrs and Min
mini=int(input("Enter the time in minutes"))
time=temp=mini
count=0
if time<60:
    print("hrs:",count,"minutes",mini)
else:
    while time>=60:
        time=time-60
        count=count+1
minites=temp-(count*60)

print("hrs",count,"min",minites)
