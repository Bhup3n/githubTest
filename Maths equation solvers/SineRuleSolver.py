import math

def findSide(angleA, b, angleB, dp):
    a = (b * math.sin(math.radians(angleA))) / (math.sin(math.radians(angleB)))
    roundedA = round(a, dp)
    print(f"\na = {a}")
    print(f"a = {roundedA}")

def findAngle(a, b, angleB, dp):
    decimalA = (a * math.sin(math.radians(angleB))) / (b) #get the decimal value of the angle
    angleA = math.degrees(math.asin(decimalA)) #get the angle
    roundedAngleA = round(angleA, dp)
    print(f"\nA = {angleA}°")
    print(f"A = {roundedAngleA}°")

while True:
    choice = input("\nfind side or find angle?\ntype 'side' for side or 'angle' for angle: ").lower()
    if choice == "side" or choice == "angle":
        break

dp = int(input("how many dp do you want to round to: "))
if choice == "side":
    angleA = float(input("\nenter angle A: "))
    sideB = float(input("enter side b: "))
    angleB = float(input("enter angle B: "))
    findSide(angleA, sideB, angleB, dp)
else:
    sideA = float(input("\nenter side a: "))
    sideB = float(input("enter side b: "))
    angleB = float(input("enter angle B: "))
    findAngle(sideA, sideB, angleB, dp)