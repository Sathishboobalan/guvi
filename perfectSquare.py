#per square or not
import math
def sqr():
    n=int(input())
    m=int(input())
    m*=n
    s=math.sqrt(m)
    if s==int(s):
        print("yes")
    else:
        print("no")
sqr()    
