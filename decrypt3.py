from Crypto.Cipher import AES
from Crypto.Util import Counter
import sys

def decrypt_aes_ctr_zero_nonce(ciphertext_path, decrypted_path, key):
    """
    Decrypts a file encrypted with AES-CTR assuming a nonce of all zeros and a 128-bit counter.

    :param ciphertext_path: Path to the encrypted file (ciphertext).
    :param decrypted_path: Path where the decrypted file will be saved.
    :param key: AES key (bytes).
    """
    try:
        # Read the ciphertext from the file
        with open(ciphertext_path, 'rb') as f:
            ciphertext = f.read()
        print(f"Ciphertext length: {len(ciphertext)} bytes")

        # Initialize the counter with a 128-bit counter and no prefix (nonce)
        # This assumes that the entire 128 bits are used for the counter with nonce=0
        ctr = Counter.new(128, initial_value=0)
        print("Counter initialized with 128-bit counter and nonce=0")

        # Initialize the AES cipher in CTR mode with the specified counter
        cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
        print("AES cipher initialized in CTR mode")

        # Decrypt the ciphertext
        plaintext = cipher.decrypt(ciphertext)
        print("Decryption completed")

        # Verify the PNG signature
        png_signature = b'\x89PNG\r\n\x1a\n'
        if plaintext.startswith(png_signature):
            print("PNG signature verified. Decryption likely successful.")
        else:
            print("PNG signature mismatch. Decryption may have failed.")

        # Write the decrypted plaintext to the output file
        with open(decrypted_path, 'wb') as out_file:
            out_file.write(plaintext)
        print(f"Decrypted file saved as '{decrypted_path}'")

    except FileNotFoundError:
        print(f"Error: The file '{ciphertext_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Define the key (must be bytes)
    key = b'sup3rrr s3cr3ttt'  # 16-byte key

    # Define paths
    ciphertext_path = 'flag.png.enc'       # Encrypted file
    decrypted_path = 'decrypted_flag.png'  # Output decrypted file

    # Call the decryption function
    decrypt_aes_ctr_zero_nonce(ciphertext_path, decrypted_path, key)