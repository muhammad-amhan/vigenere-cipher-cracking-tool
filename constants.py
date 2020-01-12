import os

ROOT_DIR = os.path.dirname(os.path.normpath(__file__))

RESULTS_FILENAME = 'results'
RESULTS_DIR_NAME = 'plaintext'

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

MAX_SHIFTS = 31

ALPHABET_LETTERS_AND_FREQUENCIES = {
    'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.127, 'F': 0.022, 'G': 0.02,
    'H': 0.061, 'I': 0.07, 'J': 0.002, 'K': 0.008, 'L': 0.04, 'M': 0.024, 'N': 0.067,
    'O': 0.075, 'P': 0.019, 'Q': 0.001, 'R': 0.06, 'S': 0.063, 'T': 0.091, 'U': 0.028,
    'V': 0.01, 'W': 0.024, 'X': 0.002, 'Y': 0.02, 'Z': 0.001,
}

ENGLISH_IC = 0.067

COMMON_WORDS = [
    'THE', 'HAVE', 'THIS', 'FROM', 'WHICH', 'HAD', 'YOU',
    'WAS', 'WITH', 'MANY', 'FOR', 'AND', 'NOT', 'WILL',
    'THEIR', 'GET', 'WHEN', 'OVER', 'ITS', 'ANY', 'SO', 'SHE',
    'HE', 'CAN', 'WILL', 'WERE', 'VERY', 'WHAT', 'WHERE',
]

