from collections import Counter

ENGLISH_FREQUENCY = {
    'e': 12.702, 't': 9.056, 'a': 8.167, 'o': 7.507, 'i': 6.966,
    'n': 6.749, 's': 6.327, 'h': 6.094, 'r': 5.987, 'd': 4.253,
    'l': 4.025, 'u': 2.758, 'c': 2.202, 'm': 2.406, 'f': 2.228,
    'y': 1.974, 'p': 1.929, 'b': 1.492, 'g': 2.015, 'v': 0.978,
    'k': 0.772, 'j': 0.153, 'x': 0.150, 'q': 0.095, 'z': 0.074
}

def get_frequency_score(text):
    text = ''.join([char.lower() for char in text if char.isalpha()])
    letter_count = Counter(text)
    total_letters = sum(letter_count.values())

    letter_frequency = {char: count / total_letters * 100 for char, count in letter_count.items()}

    score = 0
    for letter, freq in ENGLISH_FREQUENCY.items():
        score += abs(freq - letter_frequency.get(letter, 0))

    return score

def shift_text(text, shift):
    shifted_text = []
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a'))
            shifted_text.append(shifted_char if char.islower() else shifted_char.upper())
        else:
            shifted_text.append(char)
    return ''.join(shifted_text)

def decrypt_ciphertext(ciphertext):
    columns = [ciphertext[i::len(ciphertext) // 4] for i in range(len(ciphertext) // 4)]
    
    best_shift = []

    for col_index, col in enumerate(columns):
        best_col_score = float('inf')
        best_col_shift = 0
        for shift in range(26):
            shifted_column = shift_text(col, shift)
            score = get_frequency_score(shifted_column)
            print(f"Trying column {col_index}, Shift {shift}: Score = {score}")
            if score < best_col_score:
                best_col_score = score
                best_col_shift = shift
        best_shift.append(best_col_shift)

    decrypted_text = ""
    for i, char in enumerate(ciphertext):
        col_index = i % len(columns)
        decrypted_text += shift_text(char, best_shift[col_index])

    return decrypted_text

ciphertext = "alnx it uxsmv gwuir wnfof vngvgw hpk n rkgnqb loxl rt tnf fhfzcsvx xhqt, tw ni hsy'th zglnnm zjnv, jukr ctz, pbn. exb grplvabt pv hujgokqn of hivngw l kumzw."

decrypted_text = decrypt_ciphertext(ciphertext)
print("\nDecrypted text:\n", decrypted_text)
