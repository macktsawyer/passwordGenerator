import os
import json
import string
import random
from dotenv import load_dotenv

load_dotenv()
my_key = os.getenv('KEY')


def first_pass(phrase):
    matrix = []
    new_matrix = []

    for letter in phrase:
        matrix.append(letter)

    for rotate in range(len(my_key)):
        for i in range(len(matrix)):
            if i == len(matrix) - 1:
                new_matrix.append(matrix[0])
            else:
                new_matrix.append(matrix[i + 1])
        matrix = new_matrix
        new_matrix = []

    end_result = string_results(matrix)

    return end_result


def second_pass(phrase):
    print("phrase")
    key_dict = open(".env", "r").readlines()
    destring = key_dict[1]
    print("destring")
    print(destring)


def make_value_dict():
    key_value_dict = {}
    for al in string.ascii_letters:
        key_value_dict[al] = random.randint(0, 9)
    for al in string.digits:
        key_value_dict[al] = random.randint(0, 9)
    for al in string.punctuation:
        key_value_dict[al] = random.randint(0, 9)

    dumped = json.dumps(key_value_dict)
    print("dumped")

    overwrite_key(dumped, '.env')


def overwrite_key(intake, file):
    stringify = str(intake)

    with open(file, "r") as f:
        temp = f.readlines()
        f.close()

    temp[0] = temp[0].replace('\n', '')

    output = open(file, "w")
    output.write(f'{temp[0]}\nkey_value = {stringify}')
    output.flush()
    os.fsync(output.fileno())


def string_results(list_array):
    enc_string = ''
    for new in list_array:
        enc_string = enc_string + new

    return enc_string


def encryption(phrase):
    first = first_pass(phrase)
    print("first")
    make_value_dict()
    second_pass(first)
    return first
