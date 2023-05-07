import os
import utils
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

    end_result = string_first_layer(matrix)

    return end_result


def second_pass(phrase):
    key_dict = open(".env", "r").readlines()
    string = key_dict[1]
    filtered_dict = utils.string_dict(string)
    print(phrase)
    print(filtered_dict)


def string_first_layer(list_array):
    enc_string = ''
    for new in list_array:
        enc_string = enc_string + new

    return enc_string


def encryption(phrase):
    first = first_pass(phrase)
    utils.make_value_dict()
    second_pass(first)
    return first
