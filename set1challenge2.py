#!/usr/bin/env python3

"""Fixed XOR - https://cryptopals.com/sets/1/challenges/2"""

STRING_1 = "1c0111001f010100061a024b53535009181c"
STRING_2 = "686974207468652062756c6c277320657965"
RESULT = "746865206b696420646f6e277420706c6179"


def xor_strings(a, b):
    """XOR two hexadecimal strings."""
    result = int(a, 16) ^ int(b, 16)
    return '{:x}'.format(result)

print(xor_strings(STRING_1, STRING_2) == RESULT)
