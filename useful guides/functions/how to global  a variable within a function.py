def area_circle(pi, r):
    global a   #you have to declare the variable to be global before you start using the variable
    a = pi * r**2
    return a
pi = 3.14
radius = 4

area_circle(pi, radius)
print("this is proof that i have globalised a:", a)