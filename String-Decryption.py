# Ralph Lorenz I. Codilan
# BSCpE 1-5
# Object-Oriented Programming - Assignment 2 - #2

import pyfiglet
import time
from colorama import init, Fore, Style
from tqdm import tqdm

init() # Initialize colorama module

while True:
    encrypted_text = input("Enter a string to decrypt: ")

    # Create a dictionary for decryption
    decrypt_dict = {'*': 'a', '&': 'e', '#': 'i', '+': 'o', '!': 'u'}

    # Decrypt the text using the dictionary
    decrypted_text = ""
    for char in encrypted_text:
        if char in decrypt_dict:
            decrypted_text += decrypt_dict[char]
        else:
            decrypted_text += char