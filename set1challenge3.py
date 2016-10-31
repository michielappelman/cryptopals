#!/usr/bin/env python3

"""Single-byte XOR cipher - https://cryptopals.com/sets/1/challenges/3"""

import string
from binascii import unhexlify, hexlify

STRING = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
COMMON = "etaoins"


def xor_strings_single_chr(s, character):
    """XOR a hex string with one character, returns a new hex string."""
    xor = [chr(ord(b) ^ ord(character)) for b in unhexlify(s)]
    joined = "".join(xor)
    return hexlify(joined)

contenders = []

for c in string.printable:
    result = unhexlify(xor_strings_single_chr(STRING, c))

    # Only look at results where all characters are actually printable.
    if all(a in string.printable for a in result):
        # Count the number of characters also most common English characters.
        count = len([p for p in result.lower() if p in COMMON])
        contenders.append((c, result, int(count)))

# Pick the contender with the highest number of common characters.
PROBABLY = max(contenders, key=lambda x: x[2])

print("{}: {}".format(PROBABLY[0], PROBABLY[1]))