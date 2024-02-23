import math

def area(a, b, angleC, dp):
    area = 0.5 * (a) * (b) * (math.sin(math.radians(angleC)))
    roundedArea = round(area, dp)
    print(f"area = {area}")
    print(f"area = {roundedArea}")

a = float(input("enter a: "))
b = float(input("enter b: "))
angleC = float(input("enter angle C: "))
dp = int(input("how many decimal places: "))

area(a, b, angleC, dp)