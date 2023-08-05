from string import ascii_uppercase, ascii_lowercase, digits
from itertools import chain

# creates table defined in RFC 4648
# https://en.wikipedia.org/wiki/Base64
def create_table():
    table = dict()

    for i, c in enumerate(chain(ascii_uppercase, ascii_lowercase, digits, "+", "/")):
        table[tuple(format(i, "06b"))] = c
    table["padding"] = "="
    return table
