#!/usr/bin/env python3
# Based on research by Larsenv from RiiConnect24
from glob import glob
import os
import sys

from Crypto.Cipher import AES

# Thanks to Larsenv for figuring these out!
key = b"\x01\x67\x68\x54\xAC\x6A\x40\x49\xBE\x12\x49\x75\xA9\xE2\x23\x3E\x96\xBC\xE6\x19\xBF\xD6\x47\x2E\xBD\x27\x78\x93\x3C\x10\xFF\xE5"
iv = b"\xA0\x3F\x89\xFA\x97\x76\x47\xDB\xB4\x2A\xCF\x16\xEA\xB6\xDB\x3E"

if not os.path.exists("zipcode"):
    print("Please put all your zipcode files in a subdirectory of the \"zipcode\" directory!")
    sys.exit(0)

for subdirectory in glob(os.path.join("zipcode", "*")):
    decrypted_dir = os.path.join(subdirectory, "decrypted")
    if not os.path.exists(decrypted_dir):
        os.makedirs(decrypted_dir)
    for dat_file in glob(os.path.join(subdirectory, "*.dat")):
        print("Decrypting " + dat_file + "...")
        with open(dat_file, "rb") as infile:
            encrypted_file = infile.read()
            decrypted_file = AES.new(key, AES.MODE_CBC, iv).decrypt(encrypted_file[320:])
        with open(os.path.join(decrypted_dir, os.path.basename(dat_file)), "wb") as outfile:
            outfile.write(decrypted_file[25:])

print("Operation completed.")
