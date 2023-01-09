# =========== OPTION 1 ================
import sys

# Parse command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]
cypherkey = sys.argv[3] if len(sys.argv) > 3 else open('cypherkey.txt').read()

# Read in the contents of the first file
with open(input_file, 'r') as f:
    data = f.read()

# Encrypt the data using the XOR cipher
encrypted = ''.join(chr(ord(c) ^ ord(cypherkey[i % len(cypherkey)])) for i, c in enumerate(data))

# Write the encrypted data to the second file
with open(output_file, 'w') as f:
    f.write(encrypted)

print(f"\n\x1b[32mSuccessfully encrypted your \x1b[33m{input_file} \x1b[32mfile and wrote the result to \x1b[33m{output_file} \x1b[32mfile \n") 



# =========== OPTION 2 with asking name of files ================
# from hashlib import sha256

# file_in = input('File to encrypting / decrypting (file.txt) : ')
# file_out = input('Output file name : ')
# key = sha256(input('Password : ').encode('utf-8')).digest()

# with open(file_in, 'rb') as f_in:
#     with open(file_out, 'wb') as f_out:
#         i = 0
#         while f_in.peek():
#             b = bytes([ord(f_in.read(1)) ^ key[i % len(key)]])
#             f_out.write(b)
#             i += 1
