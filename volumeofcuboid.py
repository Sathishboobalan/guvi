#volume of cuboid
def cuboid_volume(l,b,h):
    if(l<0 or b<0 or h<0):
        invalid()
    else:
        print("volume:",l*b*h)
def invalid():
    print("invalid input")
l=float(input())
b=float(input())
h=float(input())
cuboid_volume(l,b,h)
