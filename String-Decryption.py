# Ralph Lorenz I. Codilan
# BSCpE 1-5
# Object-Oriented Programming - Assignment 2 - Problem 2

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
    
    # Print the decrypted text with a colorful pyfiglet title
    title = pyfiglet.figlet_format("Decrypted Text")
    print(Fore.BLUE + title)

    # Print the decrypted text with alternating colors for each character
    for i in tqdm(range(len(decrypted_text))):
        if i % 2 == 0:
            print(Fore.GREEN + decrypted_text[i], end = '')
        else:
            print(Fore.MAGENTA + decrypted_text[i], end = '')
        time.sleep(0.05)
    
    # Reset colorama style
    print(Style.RESET_ALL)

    # Ask user if they want to try again
    while True:
        answer = input("Do you want to decrypt another string? (y/n) ")
        if answer.lower() == 'y':
            break
        elif answer.lower() == 'n':
            print(Fore.YELLOW + pyfiglet.figlet_format("Goodbye!"))
            time.sleep(1.00)
            exit()
        else:
            print(Fore.RED + "Invalid input. Please enter 'y' or 'n'.")

# Program is now complete