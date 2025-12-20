this is a pretty cool encryption/cipher algorithm.

first i need to get this out of the way
this is NOT an alternative for real encryptions algorithms such as aes, it's just a project i found cool.

the ciper.py and decipher.py use the least advanced algorithm, it's a simple alphabet-shift cipher that shifts based on a key number
the cipherupgraded.py and decipherupgraded.py use a better version with hashing instead of a hard-coded key (all the other versions below this also use hashing)
the cipherevenbetter.py and decpherevenbetter.py use an even better version with a nonce meaning even with the same passphrase and data, the ciphertext is never the same
the cipherinsane.py and decipherinsane.py use the best version with authentication
the cipherfile.py and decipherfile.py use a similar version to the ciperinsane.py and decipherinsane.py but it encrypts the raw bytes of files instead of just text, meaning it can encrypt any file.

i have a little project for you, try to decrypt the image i have left you. (don't go looking for the passphrase or fragments of the passphrase i forgot it so i couldn't possibly give it to you)