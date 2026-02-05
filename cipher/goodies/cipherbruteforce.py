import string
from collections import Counter

ciphertext = input("Enter ciphertext: ")
KEY_LEN = 40
ALPHABET = string.ascii_lowercase

ENGLISH_FREQ = "etaoinshrdlcumwfgypbvkjxqz"

def shift_char(c, shift):
    return chr((ord(c) - 97 - shift) % 26 + 97)

def score_english(text):
    freq = Counter(text)
    score = 0
    for i, ch in enumerate(ENGLISH_FREQ):
        score += freq.get(ch, 0) * (26 - i)
    return score

letters = []
positions = []
for i, c in enumerate(ciphertext):
    if c.isalpha():
        letters.append(c.lower())
        positions.append(i)

columns = [[] for _ in range(KEY_LEN)]
for i, c in enumerate(letters):
    columns[i % KEY_LEN].append(c)

key_digits = []
for col in columns:
    best_shift = 0
    best_score = -1
    for shift in range(10):
        decoded = ''.join(shift_char(c, shift) for c in col)
        s = score_english(decoded)
        if s > best_score:
            best_score = s
            best_shift = shift
    key_digits.append(best_shift)

print("Recovered key digits:")
print(''.join(map(str, key_digits)))

plaintext = list(ciphertext)
letter_index = 0
for i, c in enumerate(ciphertext):
    if c.isalpha():
        shift = key_digits[letter_index % KEY_LEN]
        base = 'a' if c.islower() else 'A'
        plaintext[i] = chr((ord(c) - ord(base) - shift) % 26 + ord(base))
        letter_index += 1

print("\nDecrypted plaintext:\n")
print(''.join(plaintext))
