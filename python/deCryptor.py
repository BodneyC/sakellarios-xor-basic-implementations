# =========== OPTION 1 ================
import sys

# BEN: First comment would be on input validation, whether you're making a CLI
#  tool, some REST API, a website, whatever: if a user inputs data, they will
#  almost certainly input the wrong data
#
# It is therefore your job as the programmer to specifically define what
#  those inputs may look like and reject those inputs that don't look
#  right, otherwise things might fail in surprising ways
#
# Ideally, you'd check the number of args
#
# Then, you'd check if the file exists, not immediately try to read it, if
#  not then give an error
#
# If you wanted to cover all bases, you could check the permission the
#  effective user has over the file, i.e. can they see that it exists... but
#  not read it?

# Parse command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]
cypherkey = sys.argv[3] if len(sys.argv) > 3 else open('cypherkey.txt').read()

# What if my `-f` was a 512GB drive, what does `f.read()` do with that?
#
# This is why the streaming approach is often better when dealing with files
#  out of your control - traditionally for this you'd `open` the file which
#  would yield a pointer to your current location in the file, then `read` a
#  chunk into a buffer, when you want to read more, use the same buffer and
#  lose the previous chunk - the memory footprint is then only the size of the
#  buffer
#
# In Python (and other high level languages) you could use a buffered-reader
#  which does exactly what I described above but is less fiddley and usually
#  provides lots of extra utility you don't need to write yourself, See:
#     https://stackoverflow.com/a/10199311
#
# Alternatively, in Python you couuld use a generator to chunk the data
#  yourself if you wanted to use the standard open/read approach (not from the
#  `io library`), see:
#     https://stackoverflow.com/a/519653
#
# PS. You do this with the Ruby implementation!!!

# Read in the contents of the first file
with open(input_file, 'r') as f:
    data = f.read()

# BEN: All the honeys love them sweet one-liners
#
# Were it any longer I would probably complain about readability but I think
#  this one might be the perfect length: no repeated segments to compensate for
#  a lack of variable assignments; only one comprehension; only one iteration -
#  spot on

# Encrypt the data using the XOR cipher
encrypted = ''.join(chr(ord(c) ^ ord(cypherkey[i % len(cypherkey)])) for i, c in enumerate(data))

# BEN: Say my --file was 5GB, so something that will fit in memory ignoring
# that other concern, but something that will take a while to complete
#
# I sit here for two minutes waiting for the program to encode my file, it
# moves to this line and I haven't provided a -o flag. The process exits and
# all that work is lost...
#
# It would be worth, earlier in the program having a writeability check as part
#  of your input validation, say:
#    f = open(output_file, 'a')
#    if not f.writable():
#        ...
#    f.close()

# Write the encrypted data to the second file
with open(output_file, 'w') as f:
    f.write(encrypted)

# BEN: Love the stylised output as I do, for the sake of maintainability it
#  would be worth extracting some of the escape codes to variables or even a
#  separate module
#
# This is really what most "colorize your terminal output" lbraries do, e.g.
#   https://github.com/lukeed/kleur/blob/master/colors.mjs#L13
#
# A library may be overkill, but variables for readability might not
print(f"\n\x1b[32mSuccessfully encrypted your \x1b[33m{input_file} \x1b[32mfile and wrote the result to \x1b[33m{output_file} \x1b[32mfile \n") 


# BEN: I'm glad this is commmented out :D
#
# The input() kind of input, particularly for files, means that I lose my
#  tab-completion so I'm not 100% the file I provided exists, very annoying, it
#  also is unlikely to process control key (arrows, for example)
#
# You could implemet basic readline functionality or use a library, but it's
#  not worth it unless you're writing a *very* interactive application
#
# The input() kind of input would work fine for the key, but even then I would
#  question its use. In terms of command composability, having a flag or a
#  positional makes so much more sense
#
# The closest style of input to this that is common for passwords would be via
#  stdin, e.g.
#     echo "$PASSWORD" | docker login --password-stdin

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
