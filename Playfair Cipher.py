# Playfair Cipher

m = ["MONAR", "CHYBD", "EFGIK", "LPQST", "UVWXZ"]

text = input("Enter a text: ").upper()

def pos(ch):
    if ch == 'J':
        ch = 'I'
    for i in range(5):
        for j in range(5):
            if m[i][j] == ch:
                return i, j

a, b = text[0], text[1]
r1, c1 = pos(a)
r2, c2 = pos(b)

# Encryption
if r1 == r2:
    e1 = m[r1][(c1+1)%5]
    e2 = m[r2][(c2+1)%5]
elif c1 == c2:
    e1 = m[(r1+1)%5][c1]
    e2 = m[(r2+1)%5][c2]
else:
    e1 = m[r1][c2]
    e2 = m[r2][c1]

encrypted = e1 + e2
print("Encrypted:", encrypted)

# Decryption
r1, c1 = pos(e1)
r2, c2 = pos(e2)

if r1 == r2:
    d1 = m[r1][(c1-1)%5]
    d2 = m[r2][(c2-1)%5]
elif c1 == c2:
    d1 = m[(r1-1)%5][c1]
    d2 = m[(r2-1)%5][c2]
else:
    d1 = m[r1][c2]
    d2 = m[r2][c1]

print("Decrypted:", d1 + d2)
