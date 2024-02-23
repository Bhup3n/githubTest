import math

def findSide(b, c, angleA, dp):
    a = math.sqrt(((b)**2) + ((c)**2) - (2*(b)*(c)*(math.cos(math.radians(angleA)))))
    roundedA = round(a, dp)
    print(f"\na = {a}")
    print(f"a = {roundedA}")

def findAngle(a, b, c, dp):
    decimalA = ((b)**2 + (c)**2 - (a)**2) / (2*(b)*(c))
    angleA = math.degrees(math.acos(decimalA))
    roundedAngleA = round(angleA, dp)
    print(f"\nA = {angleA}°")
    print(f"A = {roundedAngleA}°")

while True:
    choice = input("\ndo you want to find the side or angle,\nenter 'side' for side and 'angle' for angle: ").lower()
    if choice == "side" or choice == "angle":
        break

dp = int(input("how many dp to round to: "))
if choice == "side":
    angleA = float(input("enter angle A: "))
    b = float(input("enter side length b: "))
    c = float(input("enter side length c: "))
    findSide(b, c, angleA, dp)
else:
    a = float(input("enter side length a: "))
    b = float(input("enter side length b: "))
    c = float(input("enter side length c: "))
    findAngle(a, b, c, dp)