#number reverse
def num_reverse(n):
    new=0
    while n!=0:
        digi=n%10
        new=new*10+digi
        n//=10
        
    return new
num_reverse(int(input()))
