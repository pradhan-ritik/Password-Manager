import random
import os
SEED = int.from_bytes(os.urandom(8), byteorder="big")
TYPES_OF_LETTERS = tuple(["ascii_lowercase", "ascii_uppercase", "digits", "punctuation"])
random.seed(SEED)