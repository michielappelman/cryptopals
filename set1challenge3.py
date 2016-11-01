#!/usr/bin/env python3

"""Single-byte XOR cipher - https://cryptopals.com/sets/1/challenges/3"""

import string
from binascii import unhexlify, hexlify

STRING = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
LETTERS = "etaoinshrdlcumwfgypbvkjxqz"


def xor_strings_single_chr(s, character):
    """XOR a hex string with one character, returns a new hex string."""
    xor = [chr(ord(b) ^ ord(character)) for b in unhexlify(s)]
    joined = "".join(xor)
    return hexlify(joined)


def english_score(result):
    """Score the result based on letter frequency in English."""
    scores = {letter: score for score, letter in enumerate(reversed(LETTERS))}
    score = 0
    for character in result[1]:
        if str(character) in LETTERS:
            score += scores[character]
    return score

contenders = []

for c in string.printable:
    result = unhexlify(xor_strings_single_chr(STRING, c))

    # Only look at results where all characters are actually printable.
    if all(a in string.printable for a in result):
        contenders.append((c, result))

# Pick the contender with the highest number of common characters.
winner = max(contenders, key=english_score)

print("{}: {}".format(winner[0], winner[1]))
