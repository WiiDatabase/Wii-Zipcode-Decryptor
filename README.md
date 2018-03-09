Wii DAT Decryptor for "Set Personal Data Channel"
==============
This Python 3 script decrypts DAT files from the Wii's japan-only "Set Personal Data Channel" (000100084843434A).
Thanks to Larsenv from [RiiConnect24](https://rc24.xyz/) for figuring out the keys and the format!

## Usage
1. Install PyCryptodome
2. Put your encrypted DAT files in the subdirectories "zipcode/001" and "zipcode/255" (just examples, any subdir will work; also see [this repo](https://github.com/RiiConnect24/CFH/tree/master/zipcode)) of this script
3. Run decryptor.py
4. Your decrypted DAT files are in the "decrypted" subdirectory!

### And after that?
1. Decompress the LZ77 archive with [DSDecmp](https://www.romhacking.net/utilities/789/) (`dsdecmp DAT_File`)
2. ???

## Technical stuff
1. Remove the first 320 bytes (the RSA signature) from the DAT file
2. Decrypt it with AES-256-CBC mode and the key `01676854AC6A4049BE124975A9E2233E96BCE619BFD6472EBD2778933C10FFE5` with `A03F89FA977647DBB42ACF16EAB6DB3E` as initialiazation vector
3. You get a file with "zpcd" as the first bytes. Remove the first 19 bytes from the decrypted data and you get an LZ77-compressed archive
