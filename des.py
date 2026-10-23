from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'8bytekey'
iv = b'12345678'
msg = b'Hello DES'

cipher = DES.new(key, DES.MODE_CBC, iv)
encrypted = cipher.encrypt(pad(msg, 8))
print("Encrypted:", encrypted.hex())

cipher = DES.new(key, DES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(encrypted), 8)
print("Decrypted:", decrypted.decode())