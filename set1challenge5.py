#!/usr/bin/env python3

"""Implement repeating-key XOR - https://cryptopals.com/sets/1/challenges/5"""

from itertools import cycle
from binascii import unhexlify, hexlify

STANZA = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
KEY = "ICE"
RESULT = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""


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

cipher = encrypt(STANZA, KEY)
print(cipher)
print(decrypt(cipher, KEY))
