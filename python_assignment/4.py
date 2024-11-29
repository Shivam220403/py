import math
a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant: "))

x1 = (-b+math.sqrt(math.pow(b, 2) - 4*a*c))/2*a
x2 = (-b-math.sqrt(math.pow(b, 2) - 4*a*c))/2*a


print(f"The Roots of {a}x^2 +{b}x +{c} = {x1} and {x2}")
