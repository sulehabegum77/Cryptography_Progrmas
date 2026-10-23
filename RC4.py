def rc4(key, text):
    S = list(range(256))
    j = 0

    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    result = []

    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        k = S[(S[i] + S[j]) % 256]
        result.append(char ^ k)

    return bytes(result)


# Input
key = input("Enter key: ").encode()
plaintext = input("Enter plaintext: ").encode()

# Encryption
ciphertext = rc4(key, plaintext)
print("Encrypted (hex):", ciphertext.hex())

# Decryption
decrypted = rc4(key, ciphertext)
print("Decrypted text:", decrypted.decode())