from cryptography.fernet import Fernet
import base64

encrypted = input("Enter encrypted text: ").encode()
random_hex = input("Enter key: ")

random_key = bytes.fromhex(random_hex)
key = base64.urlsafe_b64encode(random_key[:32])
cipher = Fernet(key)

decrypted = cipher.decrypt(encrypted)
print("Original text:", decrypted.decode())