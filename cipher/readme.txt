Copyright (C) 2026  Turkey

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License Version 3 as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.



this is a pretty cool encryption/cipher algorithm.

the cipher.py and decipher.py use the least advanced algorithm, it's a simple alphabet-shift cipher that shifts based on a key number
the cipherupgraded.py and decipherupgraded.py use a better version with hashing instead of a hard-coded key (all the other versions below this also use hashing)
the cipherevenbetter.py and decpherevenbetter.py use an even better version with a nonce meaning even with the same passphrase and data, the ciphertext is never the same
the cipherinsane.py and decipherinsane.py use the best version with authentication
the cipherfile.py and decipherfile.py use a similar version to the ciperinsane.py and decipherinsane.py but it encrypts the raw bytes of files instead of just text, meaning it can encrypt any file.

the text versions (cipher, cipherupgraded, cipherevenbetter, cipherinsane) aren't nearly as secure as the cipherfile as they preserve structure, special characters, punctuation, and numbers.
the file version encrypts the raw bytes and it's much more secure so if you care in the slightest about security, use the file version, even for text.

in the goodies folder, there's cipherfile2.py and decipherfile2.py which are more advanced and secure versions of cipherfile.py and decipherfile.py
also, the cipherfile2.py and decipherfile2.py aren't compatible with cipherfile.py and decipherfile.py

the goodies folder is just some dev tools like keygens and crack tools

NEVER use human-generated passphrases, use computer-generated passphrases, you can generate passhrases here: https://www.keepersecurity.com/en_GB/features/passphrase-generator/ and here: https://proton.me/pass/passphrase-generator


i have a little challenge for you, try to decrypt the image i have left you. (don't go looking for the passphrase or fragments of the passphrase i forgot it so i couldn't possibly give it to you)








