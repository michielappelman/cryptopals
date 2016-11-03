#!/usr/bin/env python3

"""Break repeating-key XOR - https://cryptopals.com/sets/1/challenges/6"""

from string import printable
from base64 import b64decode
from itertools import cycle
from binascii import unhexlify, hexlify


def encrypt(string, key):
    """XOR a string with a repeating key, returns a hex string."""
    xor = [chr(ord(b) ^ ord(c)) for b, c in zip(string.strip(), cycle(key))]
    joined = "".join(xor)
    return hexlify(joined)


def decrypt(hex, key):
    """XOR a hex string with a repeating key, returns a regular string."""
    xor = [chr(ord(b) ^ ord(c)) for b, c in zip(unhexlify(hex.strip()), cycle(key))]
    joined = "".join(xor)
    return joined


def hex_to_bits(text):
    """Convert a hex string to bits."""
    bits = bin(int(text.encode(), 16))[2:]
    return bits


def hamming_distance(hex1, hex2):
    """Calculate number of differing bits between two hex strings."""
    if not len(hex1) == len(hex2):
        print("hamming_distance(): strings not of equal length!")
        return None
    non_equal_bits = [True for b1, b2 in zip(hex_to_bits(hex1), hex_to_bits(hex2)) if not b1 == b2]
    distance = len(non_equal_bits)
    return distance


def probable_keylengths(cipher, low=2, high=40):
    """Return a list of the most probable keylengths based on edit distance."""
    keylengths = []
    for keylength in range(low, high):
        # Cut ciphertext in keylength pieces.
        pieces = [cipher[i:i + keylength] for i in range(0, len(cipher), keylength)]
        counts = []
        for i in range(12):
            counts.append(float(hamming_distance(pieces[i], pieces[i + 1])) / float(keylength))
        average = sum(counts) / len(counts)
        keylengths.append((keylength, average))
    keylengths.sort(key=lambda x: x[1])
    return keylengths


def transpose(blocks, size):
    """Transpose blocks."""
    transposed = ["", ""]
    for block in blocks:
        transposed[0] += block[:2]
        transposed[1] += block[2:]
    return transposed


def english_score(result):
    """Score the result based on letter frequency in English."""
    scores = {letter: score for score, letter in enumerate(reversed(LETTERS))}
    score = 0
    for character in result[1]:
        if str(character) in LETTERS:
            score += scores[character]
    return score


with open("6.txt", "r") as input_file:
    cipher = hexlify(b64decode("".join(input_file)))

most = probable_keylengths(cipher, 4)[0][0]
pieces = [cipher[i:i + most] for i in range(0, len(cipher), most)]
transposed = transpose(pieces, most)
for blocks in transposed:
    contenders = []
    for c in printable:
        result = decrypt(blocks, c)
        print(result)
        # Only look at results where all characters are actually printable.
        if all(a in printable for a in result):
            contenders.append((c, result))
    # Pick the contender with the highest number of common characters.
    winner = max(contenders, key=english_score)

    print("{}: {}".format(winner[0], winner[1]))
