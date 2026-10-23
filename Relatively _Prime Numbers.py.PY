import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if math.gcd(a, b) == 1:
    print("Numbers are relatively prime")
else:
    print("Numbers are not relatively prime")