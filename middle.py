#printing middle value
import math
def middle():
    a=[]
    n=int(input("enter the size"))
    for i in range(n):
        a.append(int(input()))
    temp=math.floor(n/2)
    print(a[temp])
middle()
