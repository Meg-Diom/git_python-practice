import math

a = float(input("Enter the coeffitient of x squared: "))
b = float(input("Enter the coeffitient of x:" ))
c = float(input("Enter the coeffitient of the temm without x: "))

det = (b**2) - (4*a*c)

x_1 = (-b + math.sqrt(det))/(2*a)
x_2 = (-b - math.sqrt(det))/(2*a)

print(f"The solution to the quadratic equation are:\nx_1: {x_1}.\nx_2: {x_2}")
