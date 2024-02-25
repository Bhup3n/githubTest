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
    if a > 1 or a < 0:
        aPart = a
        aPartRounded = round(a, dp)
    else:
        aPart = ""
        aPartRounded = ""
    if -(b) >= 0:
        bSymbol = "+"
    else:
        bSymbol = "-"
    if c >= 0:
        cSymbol = "+"
    else:
        cSymbol = "-"

    bPartRounded = round(b, dp)
    cPartRounded = round(c, dp)
    if rounded:
        print(f"\nCSF = {aPartRounded}(x {bSymbol} {abs(bPartRounded)})² {cSymbol} {abs(cPartRounded)}")
    else:
        print(f"\nCSF = {aPart}(x {bSymbol} {abs(b)})² {cSymbol} {abs(c)}")

a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))
dp = int(input("enter how many decimal places you want: "))

findTurningPoint(a, b, c, dp)