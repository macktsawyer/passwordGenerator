import random
import datetime
import encrypt

alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
         "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$",
         "%", "^", "&", "*"]

length = input('How long of a password would you like? ')


def log_password(word):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("password_log.txt", "a") as f:
        f.write(f"{timestamp}: {word}\n")


def password_generator(leng):
    password = ''
    for x in range(int(leng)):
        letter = random.randint(0, len(alpha) - 1)
        password = password + alpha[letter]
    print(password)
    log_password(password)

def gen():
    password_generator(length)
    encrypt.encryption()
