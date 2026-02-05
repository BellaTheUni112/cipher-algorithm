import string
ALPHABET = string.ascii_lowercase
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
def cipher(message, key_number):
    key_digits = [int(d) for d in str(key_number)]
    result = []
    key_index = 0

    for char in message:
        if char.isalpha():
            shift = key_digits[key_index % len(key_digits)]
            result.append(shift_char(char, shift))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)
def decipher(message, key_number):
    key_digits = [int(d) for d in str(key_number)]
    result = []
    key_index = 0

    for char in message:
        if char.isalpha():
            shift = key_digits[key_index % len(key_digits)]
            result.append(shift_char(char, -shift))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)
if __name__ == "__main__":
    key = 7455012338432540811853944237275066253408
    plaintext = input("Input : ")

    encrypted = cipher(plaintext, key)
    decrypted = decipher(encrypted, key)

    print("Plaintext :", plaintext)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)