#string palindrome or not
def palin():
    string=input("Enter the string")
    new_string=string[::-1]
    if(string==new_string):
        print("palindrome")
    else:
        print("not palindrome")
palin()
