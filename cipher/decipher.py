cipher = input("Input ciphered text here : ")
key = "62324125442744865455772480164963380212068431328"

import string

letters = string.ascii_lowercase
key_digits = [int(d) for d in key]

result = []
k = 0

for ch in cipher:
    if ch.lower() in letters:
        shift = key_digits[k % len(key_digits)]
        k += 1
        idx = letters.index(ch.lower())
        new_idx = (idx - shift) % 26
        new_char = letters[new_idx]
        if ch.isupper():
            new_char = new_char.upper()
        result.append(new_char)
    else:
        result.append(ch)


print("".join(result))
