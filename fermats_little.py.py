a = int(input("Enter a: "))
p = int(input("Enter prime number p: "))

if p > 1 and a % p != 0:
    result = pow(a, p - 1, p)
    print("Result =", result)

    if result == 1:
        print("Fermat's theorem holds")
else:
    print("Invalid input")