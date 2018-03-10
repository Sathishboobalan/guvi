#Print in words
def print_words():
    try:
        l=['zero','one','two','three','four','five','six','seven','eight','nine','ten']
        n=int(input("Enter the number"))
        print(l[n])
    except:
        print("invalid")
print_words()
