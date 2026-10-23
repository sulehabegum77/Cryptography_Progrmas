import math

a = int(input("Enter a: "))
m = int(input("Enter modulus m: "))

if m > 1 and math.gcd(a, m) == 1:
    inverse = pow(a, -1, m)
    print("Multiplicative inverse =", inverse)
else:
    print("Inverse does not exist")