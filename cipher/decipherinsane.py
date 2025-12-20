import hashlib
import hmac

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

def decrypt_stream(ciphertext, passphrase, nonce):
    stream = keystream_generator(passphrase, nonce)
    result = []

    for char in ciphertext:
        if char.isalpha():
            result.append(shift_char(char, -next(stream)))
        else:
            result.append(char)

    return "".join(result)

def decrypt(data, passphrase):
    try:
        nonce_hex, ciphertext, tag = data.split(":", 2)
    except ValueError:
        raise ValueError("Invalid ciphertext format")

    nonce = bytes.fromhex(nonce_hex)

    expected_tag = hmac.new(
        passphrase.encode(),
        nonce + ciphertext.encode(),
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(tag, expected_tag):
        raise ValueError("Authentication failed: wrong key or tampered data")

    return decrypt_stream(ciphertext, passphrase, nonce)

if __name__ == "__main__":
    passphrase = input("Passphrase : ")
    ciphertext = input("Ciphertext : ")

    try:
        plaintext = decrypt(ciphertext, passphrase)
        print("Decrypted :", plaintext)
    except ValueError as e:
        print(e)
