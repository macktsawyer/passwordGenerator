import random
import encrypt
import decrypt
import string

confirmation_list = ["Yes", "Y", "y", "yes", "confirm", "Confirm"]

alpha = string.ascii_letters + string.digits + string.punctuation

length = input('How long of a password would you like? ')


def log_password(word):
    with open("password_log.txt", "w") as f:
        f.write(f"{word}")


def password_generator(leng):
    password = ''
    for x in range(int(leng)):
        letter = random.choice(alpha)
        password = password + letter

    return password


def gen():
    pass_phrase = password_generator(length)
    print(f'{pass_phrase} is the pass')
    encrypted = encrypt.encryption(pass_phrase)
    print(f'{encrypted} is the encrypted pass')
    log_password(encrypted)


    confirm = input('Would you like to decrypt? ')
    if confirm in confirmation_list:
        with open("password_log.txt", "r") as f:
            stored = f.read()
        decryption = decrypt.decryption(stored)
        print(f'{decryption} is the decrypted pass')

