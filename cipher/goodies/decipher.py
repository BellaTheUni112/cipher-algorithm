cipher = input("Input ciphered text here : ")
# make sure to use the correct key. some versions of the algorithm use randomly generated keys.
key = "7455012338432540811853944237275066253408"

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