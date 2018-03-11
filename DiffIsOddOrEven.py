#diff is odd or even
def diff_odd_even():
    a=int(input("frst num"))
    b=int(input("Secnd num"))
    if a>b:
        c=a-b
    else:
        c=b-a
    if c%2==0:
        print("Even")
    else:
        print("odd")
diff_odd_even()
