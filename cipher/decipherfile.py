import hashlib
import hmac
import sys

NONCE_BYTES = 12
HMAC_BYTES = 32
CHUNK_SIZE = 4096

def keystream_generator(passphrase, nonce):
    state = hashlib.sha256(passphrase.encode() + nonce).digest()
    while True:
        for b in state:
            yield b
        state = hashlib.sha256(state).digest()

def decrypt_file(input_path, output_path, passphrase):
    with open(input_path, "rb") as f:
        nonce = f.read(NONCE_BYTES)
        data = f.read()

    ciphertext = data[:-HMAC_BYTES]
    tag = data[-HMAC_BYTES:]

    mac = hmac.new(passphrase.encode(), nonce, hashlib.sha256)
    mac.update(ciphertext)

    if not hmac.compare_digest(mac.digest(), tag):
        raise ValueError("Authentication failed: wrong key or tampered file")

    stream = keystream_generator(passphrase, nonce)

    with open(output_path, "wb") as f_out:
        for i in range(0, len(ciphertext), CHUNK_SIZE):
            chunk = ciphertext[i:i+CHUNK_SIZE]
            decrypted = bytes(b ^ next(stream) for b in chunk)
            f_out.write(decrypted)

    print("File decrypted successfully.")
# put passphrase in double quotes
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python decipherfile.py <input> <output> <passphrase>")
        sys.exit(1)

    decrypt_file(sys.argv[1], sys.argv[2], sys.argv[3])
