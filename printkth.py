#printing kth value
def input_num(n):
    a=[]
    k=int(input("Enter the kth value"))
    for i in range(n):
        a.append(int(input()))
        list1=list(a)
    print("the kth value",list1[k-1])
n=int(input())
input_num(n)
