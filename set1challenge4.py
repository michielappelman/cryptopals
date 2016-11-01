#!/usr/bin/env python3

"""Detect single-character XOR - https://cryptopals.com/sets/1/challenges/4"""

import string
from binascii import unhexlify, hexlify

LETTERS = "etaoinshrdlcumwfgypbvkjxqz"


def xor_strings_single_chr(s, character):
    """XOR a hex string with one character, returns a new hex string."""
    xor = [chr(ord(b) ^ ord(character)) for b in unhexlify(s.strip())]
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

with open("4.txt", "r") as input_file:
    for line in input_file:
        for c in string.printable:
            result = unhexlify(xor_strings_single_chr(line, c))
            # Only look at results where all characters are actually printable.
            if all(a in string.printable for a in result):
                contenders.append((c, result.strip()))

# Pick the contender with the highest score.
winner = max(contenders, key=english_score)

print("{}: {}".format(winner[0], winner[1]))
