import hashlib

ALPHABET_LEN = 26

def shift_char(char, shift):
    if char.islower():
        idx = (ord(char) - ord('a') + shift) % ALPHABET_LEN
        return chr(ord('a') + idx)
    elif char.isupper():
        idx = (ord(char) - ord('A') + shift) % ALPHABET_LEN
        return chr(ord('A') + idx)
    else:
        return char

def keystream_generator(passphrase):

    state = hashlib.sha256(passphrase.encode()).digest()

    while True:
        for byte in state:
            yield byte % ALPHABET_LEN
        state = hashlib.sha256(state).digest()

def decrypt(ciphertext, passphrase):
    result = []
    stream = keystream_generator(passphrase)

    for char in ciphertext:
        if char.isalpha():
            shift = next(stream)
            result.append(shift_char(char, -shift))
        else:
            result.append(char)

    return "".join(result)

if __name__ == "__main__":
    passphrase = input("Passphrase : ")
    ciphertext = input("Ciphertext : ")

    plaintext = decrypt(ciphertext, passphrase)

    print("Decrypted :", plaintext)
