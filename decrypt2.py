from Crypto.Cipher import AES
from Crypto.Util import Counter

key = b'sup3rrr s3cr3ttt'

# Initialize counter with nonce=0
nonce = b'\x00' * 8  # Assuming 8-byte nonce
ctr = Counter.new(64, prefix=nonce, initial_value=0)
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

# Read ciphertext
with open('flag.png.enc', 'rb') as f:
    ciphertext = f.read()

# Decrypt ciphertext
plaintext = cipher.decrypt(ciphertext)

# Save decrypted flag
with open('decrypted_flag.png', 'wb') as out_file:
    out_file.write(plaintext)

print("Decryption attempted with nonce=0. Check 'decrypted_flag.png'.")