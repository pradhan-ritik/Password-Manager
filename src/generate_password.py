from constants import *
import random
import string

def generate_password(length: int = 14) -> str:
    password_structure = []
    for i in range(length):
        password_structure.append(TYPES_OF_LETTERS[i % 4])

    random.shuffle(password_structure)

    password = ""
    for letter_type in password_structure:
        password += random.choice(getattr(string, letter_type))

    return password

