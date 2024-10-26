import subprocess
import itertools
import sys
import os
from tqdm import tqdm

def run_xorro(input_bytes, xorro_path="./xorro"):
    """
    Runs the xorro binary with the given input bytes followed by a newline.

    Args:
        input_bytes (bytes): The input bytes to send to xorro.
        xorro_path (str): Path to the xorro executable.

    Returns:
        bool: True if xorro did not crash, False otherwise.
    """
    try:
        # Execute xorro with the input bytes followed by a newline
        result = subprocess.run(
            [xorro_path],
            input=input_bytes + b'\n',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5  # Prevent hanging on unexpected inputs
        )
        
        # Check if the process was terminated by a signal (e.g., SIGSEGV)
        if result.returncode < 0:
            # Process was terminated by a signal
            return False
        else:
            # Process exited normally
            return True

    except subprocess.TimeoutExpired:
        # If xorro hangs, consider it a failure and terminate the process
        return False
    except Exception as e:
        print(f"An error occurred while running xorro: {e}")
        return False

def generate_inputs(max_length, charset=None):
    """
    Generator that yields all possible byte sequences up to max_length.

    Args:
        max_length (int): Maximum length of the input bytes.
        charset (iterable, optional): Iterable of byte values to include. Defaults to all possible bytes.

    Yields:
        bytes: The next byte sequence.
    """
    if charset is None:
        # All possible byte values from 0x00 to 0xFF
        charset = range(256)
    
    for length in range(1, max_length + 1):
        # tqdm provides a progress bar for each length
        for seq in tqdm(itertools.product(charset, repeat=length), 
                        total=256**length, 
                        desc=f"Trying length {length}"):
            yield bytes(seq)

def main():
    """
    Main function to perform brute-force on the xorro binary.
    """
    if len(sys.argv) != 3:
        print("Usage: python brute_force_xorro.py <path_to_xorro> <max_input_length>")
        print("Example: python brute_force_xorro.py ./xorro 3")
        sys.exit(1)
    
    xorro_path = sys.argv[1]
    max_length = int(sys.argv[2])

    if not os.path.isfile(xorro_path):
        print(f"Error: The file '{xorro_path}' does not exist or is not executable.")
        sys.exit(1)
    
    if not os.access(xorro_path, os.X_OK):
        print(f"Error: The file '{xorro_path}' is not executable.")
        sys.exit(1)

    print(f"Starting brute-force on '{xorro_path}' with maximum input length {max_length}...\n")

    for input_bytes in generate_inputs(max_length):
        success = run_xorro(input_bytes, xorro_path)
        if success:
            print("\n[+] Success! The following input did NOT cause a crash:")
            # Display the input in a readable format
            # Non-printable bytes will be shown in hexadecimal
            readable_input = ''.join([chr(b) if 32 <= b <= 126 else f'\\x{b:02x}' for b in input_bytes])
            print(f"Input: {readable_input}")
            sys.exit(0)
    
    print("\n[-] Brute-force completed. No successful input found within the specified parameters.")

if __name__ == "__main__":
    main()