import math

def findTurningPoint(a, b, c, dp):
    turningPointX = -((b / a) / 2)
    turningPointY = (a*(-(abs(turningPointX)**2))) + c

    findX(a, turningPointX, turningPointY, dp)

def findX(a, tpX, tpY, dp):
    x1 = (tpX + math.sqrt(abs(tpY / a)))
    x2 = (tpX - math.sqrt(abs(tpY / a)))

    rounded = False
    findCompletedSquareForm(a, tpX, tpY, dp, rounded)
    print(f"TP = ({tpX}, {tpY})")
    print(f"x = {tpX} ± √{abs(tpY / a)}")
    print(f"x = {x1}   or   x = {x2}")

    rounded = True
    findCompletedSquareForm(a, tpX, tpY, dp, rounded)
    print(f"TP = ({round(tpX, dp)}, {round(tpY, dp)})")
    print(f"x = {round(tpX, dp)} ± √{round(abs(tpY / a), dp)}")
    print(f"x = {round(x1, dp)}   or   x = {round(x2, dp)}")

def findCompletedSquareForm(a, b, c, dp, rounded):
    if rounded:
        if a > 1 and c >= 0:
            print(f"\nCSF = {round(a, dp)}(x + {-(round(b, dp))})² + {round(c, dp)}")
        elif a > 1 and c < 0:
            print(f"\nCSF = {round(a, dp)}(x + {-(round(b, dp))})² - {round(abs(c), dp)}")
        elif a == 1 and c >= 0:
            print(f"\nCSF = (x + {-(round(b, dp))})² + {round(c, dp)}")
        else:
            print(f"\nCSF = (x + {-(round(b, dp))})² - {round(abs(c), dp)}")
    else:
        if a > 1 and c >= 0:
            print(f"\nCSF = {a}(x + {-(b)})² + {c}")
        elif a > 1 and c < 0:
            print(f"\nCSF = {a}(x + {-(b)})² - {abs(c)}")
        elif a == 1 and c >= 0:
            print(f"\nCSF = (x + {-(b)})² + {c}")
        else:
            print(f"\nCSF = (x + {-(b)})² - {abs(c)}")

a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))
dp = int(input("enter how many decimal places you want: "))

findTurningPoint(a, b, c, dp)