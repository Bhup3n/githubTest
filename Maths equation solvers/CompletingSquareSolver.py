import math

def findTurningPoint(a, b, c, dp):
    turningPointX = -((b / a) / 2)
    turningPointY = (a*(-(abs(turningPointX)**2))) + c

    print(f"\nTP = ({turningPointX}, {turningPointY})")
    findX(a, turningPointX, turningPointY, dp)

def findX(a, tpX, tpY, dp):
    x1 = (tpX + math.sqrt(abs(tpY / a)))
    x2 = (tpX - math.sqrt(abs(tpY / a)))
    print(f"x = {tpX} ± √{abs(tpY / a)}")
    print(f"x = {x1}   or   x = {x2}")

    print(f"\nTP = ({round(tpX, dp)}, {round(tpY, dp)})")
    print(f"x = {round(tpX, dp)} ± √{round(abs(tpY / a), dp)}")
    print(f"x = {round(x1, dp)}   or   x = {round(x2, dp)}")

a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))
dp = int(input("enter how many decimal places you want: "))

findTurningPoint(a, b, c, dp)