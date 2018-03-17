def main():
    n=int(input())
    k=int(input())
    a=[]
    for i in range(n):
        a.append(int(input()))
    print(check(a,k))
def check(a,k):
    if k in a:
        return "yes"
    else:
        return "no"

main()
