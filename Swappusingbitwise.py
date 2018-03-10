#swapping of two numbers using bitwise
def swap(i,j):
    i=i^j
    j=i^j
    i=i^j
    print("i=",i,"j=",j)

i=int(input("Enter the first number"))
j=int(input("Enter the second number"))
swap(i,j)
