import random
from cryptography.fernet import Fernet  # type:ignore
import time
import string
import os


min_length = int(input("Enter the minimum length of you password : "))
max_length = input("Enter the maximum length of your password : ")


def password_generator(min_length, max_length,  numbers=False, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria:
        new_char = random.choice(characters)
        pwd += new_char
        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        meets_criteria = int(min_length) < len(pwd) < int(max_length)
        if numbers:
            meets_criteria = has_numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special
    return pwd


numbers = input("Do you want numbers in your password?").lower() == "y"
special_characters = input(
    "Do you want special characters in your password?").lower() == "y"


def main():
    pwd = password_generator(min_length, max_length)

    print(pwd)
    print(len(pwd))


if __name__ == "__main__":
    main()
