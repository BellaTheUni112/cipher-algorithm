import hashlib
import hmac
import secrets
import sys

NONCE_BYTES = 12
CHUNK_SIZE = 4096

def keystream_generator(passphrase, nonce):
    state = hashlib.sha256(passphrase.encode() + nonce).digest()
    while True:
        for b in state:
            yield b
        state = hashlib.sha256(state).digest()

def encrypt_file(input_path, output_path, passphrase):
    nonce = secrets.token_bytes(NONCE_BYTES)
    stream = keystream_generator(passphrase, nonce)
    mac = hmac.new(passphrase.encode(), nonce, hashlib.sha256)

    with open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
        f_out.write(nonce)

        while chunk := f_in.read(CHUNK_SIZE):
            encrypted = bytes(b ^ next(stream) for b in chunk)
            mac.update(encrypted)
            f_out.write(encrypted)

        f_out.write(mac.digest())

    print("File encrypted successfully.")
# put the passphrase in double quotes
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python cipherfile.py <input> <output> <passphrase>")
        sys.exit(1)

    encrypt_file(sys.argv[1], sys.argv[2], sys.argv[3])
