import sys
from constants import ALPHABET
from typing import List

ENCRYPT = 'encrypt'
DECRYPT = 'decrypt'

operations = {
    1: ENCRYPT,
    2: DECRYPT,
    3: 'exit',
}

operations_prompt = {
    1: 'Plain Text',
    2: 'Cipher Text',
    3: 'Thank you for using Vigenère Cipher',
}


class InvalidSecretKey(Exception):
    pass


def validate_keyword(keyword: str):
    if not keyword:
        raise InvalidSecretKey('A valid secret key is required')

    if not all(x.isalpha() or x.isspace() or x.isupper() for x in keyword):
        raise InvalidSecretKey(f'Secret key must comprise of capital English letters: {keyword}')


def expand_keyword(data_text: str, keyword: str) -> str:
    validate_keyword(keyword)
    expanded_keyword = ''

    for index, letter in enumerate(data_text):
        if letter.isspace():
            expanded_keyword += ' '

        expanded_keyword += keyword[index % len(keyword)]
    return expanded_keyword


def calculate_shift_keys(keyword: str) -> List[int]:
    return [
        ALPHABET.find(keyword_letter) - ALPHABET.find('A')
        for keyword_letter
        in keyword
    ]


def perform_operation(text_data: str, keyword: str, mode: str) -> str:
    try:
        expanded_keyword = expand_keyword(text_data, keyword)
        shift_keys = calculate_shift_keys(expanded_keyword)

        return process_text_data(text_data, shift_keys, mode)
    except ValueError as e:
        print(e)


def process_text_data(text_data: str, shift_keys: List[int], mode: str) -> str:
    result_text_data = ''

    for shift_key, text_letter in zip(shift_keys, text_data):
        if text_letter.isspace():
            result_text_data += ' '
            continue

        text_letter_index_in_alphabet = ALPHABET.find(text_letter)

        if mode == ENCRYPT:
            result_text_data += ALPHABET[(text_letter_index_in_alphabet + shift_key) % 26]

        elif mode == DECRYPT:
            result_text_data += ALPHABET[(text_letter_index_in_alphabet - shift_key) % 26]

    return result_text_data


class InvalidOption(Exception):
    pass


if __name__ == '__main__':
    print('*********** Vigenère Cipher ***********\n')

    while True:
        try:
            if (input_mode := int(input('1. Encrypt\n'
                                        '2. Decrypt\n'
                                        '3. Exit\n'
                                        'Option: '))) in operations.keys():
                if input_mode == 3:
                    print(operations_prompt[input_mode])
                    sys.exit(0)

                text_input = input(f'* {operations_prompt[input_mode]}: ').upper()
                keyword_input = input('* Secret Key: ').upper()

                text_output = perform_operation(text_input, keyword_input, operations[input_mode])
                print(f'* {operations_prompt[input_mode]}: <<{text_output}>>\n')

            else:
                raise InvalidOption('Choose from available options.\n')

        except ValueError as e:
            print(f'Option must be a number (integer).\n')

        except InvalidOption as e:
            print(f'{str(e)}\n')

        except InvalidSecretKey as e:
            print(f'{str(e)}\n')

