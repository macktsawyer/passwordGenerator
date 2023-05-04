import os
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

    end_result = string_results(matrix)

    return end_result


def string_results(list_array):
    enc_string = ''
    for new in list_array:
        enc_string = enc_string + new

    return enc_string


def decryption(phrase):
    first = first_pass(phrase)
    return first
