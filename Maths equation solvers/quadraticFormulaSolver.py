import math

def quadraticSolver(a, b, c, roundDecimal):
    x1 = ((-(b)) + (math.sqrt(((b)**2) - (4*(a)*(c))))) / (2*(a))
    x1Rounded = round(x1, roundDecimal)
    x2 = ((-(b)) - (math.sqrt(((b)**2) - (4*(a)*(c))))) / (2*(a))
    x2Rounded = round(x2, roundDecimal)
    print(f"x = {x1} , x = {x2}")
    print(f"x = {x1Rounded} , x = {x2Rounded}")

a = float(input("what is the value of a: "))
b = float(input("what is the value of b: "))
c = float(input("what is the value of c: "))
roundDecimal = int(input("how many dp do you want to round to: "))

quadraticSolver(a, b, c, roundDecimal)