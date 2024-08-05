# USING LAMBDA FUNCTION
areaa = lambda b, h: (0.5 * b * h)
print(areaa(4, 5))
perii = lambda a, b, c: (a+b+c)
print(perii(4, 5, 7))

# USING DEF FUNCTION


def area(b, h):
    a = 0.5 * b * h
    return a


def peri(a, b, c):
    p = a + b + c
    return p


print("To calculate the area of the triangle please enter the length of the base and height")
base = int(input("Base: "))
height = int(input("Height: "))
print(f"Area = {area(base,height)}")
print("To calculate the perimeter of the triangle please also enter the length of the slant")
slant = int(input("Slant: "))
print(f"Perimeter = {peri(base,height,slant)}")
