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
            new_matrix.append(matrix[i - 1])
        matrix = new_matrix
        new_matrix = []

    end_result = string_a_list(matrix)

    return end_result


def second_pass(phrase):
    matrix = []
    new_matrix = []

    for letter in phrase:
        matrix.append(letter)

    key_dict = open(".env", "r").readlines()
    string = key_dict[1]
    filtered_dict = utils.string_dict(string)

    for char in matrix:
        value = filtered_dict[char]
        index_of = matrix.index(char)
        for times in range(value):
            index_of = index_of + 3
            if index_of > len(matrix) - 1:
                index_of = index_of - 10
        print(index_of)

    # phrase = string_a_list(listed_phrase)

    return phrase


def string_a_list(list_array):
    enc_string = ''
    for new in list_array:
        enc_string = enc_string + new

    return enc_string


def decryption(phrase):
    second = second_pass(phrase)
    first = first_pass(second)

    return first
