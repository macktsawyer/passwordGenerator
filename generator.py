import random
import datetime
import encrypt
import decrypt
import string

confirmation_list = ["Yes", "Y", "y", "yes", "confirm", "Confirm"]

alpha = string.ascii_letters + string.digits + string.punctuation

length = input('How long of a password would you like? ')


def log_password(word):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("password_log.txt", "a") as f:
        f.write(f"{timestamp}: {word}\n")


def password_generator(leng):
    password = ''
    for x in range(int(leng)):
        letter = random.choice(alpha)
        password = password + letter

    return password

def gen():
    pass_phrase = password_generator(length)
    encrypted = encrypt.encryption(pass_phrase)
    print(pass_phrase)
    log_password(encrypted)

    confirm = input('Would you like to decrypt? ')
    if confirm in confirmation_list:
        decryption = decrypt.decryption(encrypted)
        print(decryption)
