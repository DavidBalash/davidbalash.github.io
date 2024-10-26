from Crypto.Cipher import AES
from Crypto.Util import Counter
import sys

# Known values
key = b'sup3rrr s3cr3ttt'
known_plaintext = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

# Read ciphertext
with open('flag.png.enc', 'rb') as f:
    ciphertext = f.read()

# Recover the first 8 bytes of the keystream
keystream_initial = bytes([c ^ p for c, p in zip(ciphertext[:8], known_plaintext)])

# Attempt to find the nonce
# Assuming nonce is 8 bytes, iterate through possible nonce values
# For practicality in a CTF, we might limit the search space
from itertools import product
import string

# Example: Assuming nonce consists of printable ASCII characters
possible_chars = string.ascii_letters + string.digits
found = False

for nonce_tuple in product(possible_chars, repeat=8):
    nonce = ''.join(nonce_tuple).encode()
    # Initialize counter with nonce and initial counter value 0
    ctr = Counter.new(64, prefix=nonce, initial_value=0)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    keystream = cipher.encrypt(b'\x00' * 16)  # Encrypt zero bytes to get keystream
    if keystream.startswith(keystream_initial):
        print(f"Possible nonce found: {nonce}")
        # Now decrypt the entire ciphertext
        cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
        plaintext = cipher.decrypt(ciphertext)
        with open('decrypted_flag.png', 'wb') as out_file:
            out_file.write(plaintext)
        print("Decryption successful. Flag saved as 'decrypted_flag.png'.")
        found = True
        break

if not found:
    print("Nonce not found within the searched range.")