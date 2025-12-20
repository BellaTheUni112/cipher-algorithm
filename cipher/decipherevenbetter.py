import hashlib

ALPHABET_LEN = 26

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

def decrypt(ciphertext, passphrase):
    nonce_hex, encrypted = ciphertext.split(":", 1)
    nonce = bytes.fromhex(nonce_hex)

    stream = keystream_generator(passphrase, nonce)

    result = []
    for char in encrypted:
        if char.isalpha():
            result.append(shift_char(char, -next(stream)))
        else:
            result.append(char)

    return "".join(result)

if __name__ == "__main__":
    passphrase = input("Passphrase : ")
    ciphertext = input("Ciphertext : ")

    print("Decrypted :", decrypt(ciphertext, passphrase))
