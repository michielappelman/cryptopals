#!/usr/bin/env python3

"""Detect single-character XOR - https://cryptopals.com/sets/1/challenges/4"""

import string
from binascii import unhexlify, hexlify

COMMON = "etaoins"


def xor_strings_single_chr(s, character):
    """XOR a hex string with one character, returns a new hex string."""
    xor = [chr(ord(b) ^ ord(character)) for b in unhexlify(s.strip())]
    joined = "".join(xor)
    return hexlify(joined)

contenders = []

with open("4.txt", "r") as input_file:
    for line in input_file:
        for c in string.printable:
            result = unhexlify(xor_strings_single_chr(line, c))
            # Only look at results where all characters are actually printable.
            if all(a in string.printable for a in result):
                # Count the number of characters also most common English characters.
                count = len([p for p in result.lower() if p in COMMON])
                contenders.append((c, result, int(count)))

# Pick the contender with the highest number of common characters.
PROBABLY = max(contenders, key=lambda x: x[2])

print("{}: {}".format(PROBABLY[0], PROBABLY[1]))
