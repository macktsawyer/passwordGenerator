import string
import random
import json
import os


def make_value_dict():
    key_value_dict = {}
    for al in string.ascii_letters:
        key_value_dict[al] = random.randint(0, 9)
    for al in string.digits:
        key_value_dict[al] = random.randint(0, 9)
    for al in string.punctuation:
        key_value_dict[al] = random.randint(0, 9)

    dumped = json.dumps(key_value_dict)

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


def string_dict(dict_info):
    split_string = dict_info.split(' = ')
    value_dict = split_string[1]
    string_no_more = json.loads(value_dict)

    return string_no_more

