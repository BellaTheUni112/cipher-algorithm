import hashlib
import hmac
import secrets

ALPHABET_LEN = 26
NONCE_BYTES = 8  # 64-bit nonce

def shift_char(char, shift):
    if char.islower():
        return chr((ord(char) - 97 + shift) % 26 + 97)
    elif char.isupper():
        return chr((ord(char) - 65 + shift) % 26 + 65)
    return char

def keystream_generator(passphrase, nonce):
    seed = passphrase.encode() + nonce
    state = hashlib.sha256(seed).digest()

    while True:
        for byte in state:
            yield byte % ALPHABET_LEN
        state = hashlib.sha256(state).digest()

def encrypt_stream(message, passphrase, nonce):
    stream = keystream_generator(passphrase, nonce)
    result = []

    for char in message:
        if char.isalpha():
            result.append(shift_char(char, next(stream)))
        else:
            result.append(char)

    return "".join(result)

def encrypt(message, passphrase):
    nonce = secrets.token_bytes(NONCE_BYTES)
    ciphertext = encrypt_stream(message, passphrase, nonce)

    tag = hmac.new(
        passphrase.encode(),
        nonce + ciphertext.encode(),
        hashlib.sha256
    ).hexdigest()

    return f"{nonce.hex()}:{ciphertext}:{tag}"

if __name__ == "__main__":
    passphrase = input("Passphrase : ")
    plaintext = input("Input      : ")

    encrypted = encrypt(plaintext, passphrase)

    print("Encrypted :", encrypted)
