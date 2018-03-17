#printing special char
def special():
    count=0
    string=input()
    special='!@#$%^&*'
    specialchar=list(special)
    string=list(string)
    for x in string:
        if x in specialchar:
            count+=1
    print(count)
special()
