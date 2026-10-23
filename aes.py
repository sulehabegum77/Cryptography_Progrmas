from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
msg = b'Hello AES'

encrypted, tag = cipher.encrypt_and_digest(msg)
print("Encrypted:", encrypted.hex())

cipher2 = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher2.decrypt_and_verify(encrypted, tag)
print("Decrypted:", decrypted.decode())