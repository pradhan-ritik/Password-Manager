import random
import os
SEED = int.from_bytes(os.urandom(8), byteorder="big")
random.seed(SEED)

TYPES_OF_LETTERS = tuple(["ascii_lowercase", "ascii_uppercase", "digits", "punctuation"])
DATA_FOLDER = ".data"
logged_in = False

WARNING_TEXT_DOT_DATA = \
"""
Hello There. 
Please do not delete anything in this folder. 
If you do, it will delete all of your saved passwords and it will reset the entire program (for security).
If you want to reset your password or delete your passwords, please do it through the program.
If you have any issues please create a new issue in https://github.com/pradhan-ritik/Password-Manager/issues
"""

DELETE_DOT_DATA_TEXT = \
"""
One of the files in .data is missing.
This will mean that the 
"""