#kth smallest number
def sorting(a,k):
    a.sort()
    return a[k-1]
n=int(input())
k=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
print(sorting(a,k))
