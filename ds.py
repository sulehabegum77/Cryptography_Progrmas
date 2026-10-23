from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Generate keys
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

# Message
message = b"Hello World"

# Create digital signature
signature = private_key.sign(
    message,
    hashes.SHA256()
)
print("Signature created")

# Verify signature
try:
    public_key.verify(signature, message, hashes.SHA256())
    print("Signature is valid")
except Exception:
    print("Signature is invalid")