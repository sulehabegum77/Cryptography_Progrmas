# Diffie-Hellman Key Exchange

# Public values
p = 23
g = 5

# Private keys
a = 6
b = 15

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

# Shared secret keys
key_Alice = pow(B, a, p)
key_Bob = pow(A, b, p)

print("Public prime (p):", p)
print("Generator (g):", g)
print("Alice's public key:", A)
print("Bob's public key:", B)
print("Alice's shared key:", key_Alice)
print("Bob's shared key:", key_Bob)

if key_Alice == key_Bob:
    print("Key exchange successful")
else:
    print("Key exchange failed")