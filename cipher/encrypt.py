from cryptography.fernet import Fernet
import base64
import os

random_key = os.urandom(32)

key = base64.urlsafe_b64encode(random_key[:32])
cipher = Fernet(key)

text = input("Enter text: ").encode()
encrypted = cipher.encrypt(text)

print("Key (keep this!):", random_key.hex())
print("Encrypted:", encrypted.decode())