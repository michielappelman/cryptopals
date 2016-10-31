#!/usr/bin/env python3

"""Convert hex to base64 - https://cryptopals.com/sets/1/challenges/1"""

STRING = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
RESULT = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n"

print(STRING.decode("hex").encode("base64") == RESULT)