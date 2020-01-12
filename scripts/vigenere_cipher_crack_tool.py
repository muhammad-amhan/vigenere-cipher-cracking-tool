from collections import Counter, OrderedDict
import numpy as np
from typing import (
    List,
    Dict,
    OrderedDict as OrderedD,
    Any,
    Tuple,
    Union,
)
from utils.file_manager import save_to_file
from scripts.vigenere_cipher_tool import (
    process_text_data,
    expand_keyword,
    calculate_shift_keys,
    DECRYPT,
)
from constants import (
    ALPHABET_LETTERS_AND_FREQUENCIES,
    ALPHABET,
    COMMON_WORDS,
    MAX_SHIFTS,
)


class InvalidInput(Exception):
    pass


def analyze_shifts_ic_intervals(shifts_and_avg_ic: Dict[int, float]) -> List[Union[int, float]]:
    highest_avg_ics = sorted(shifts_and_avg_ic.values(), reverse=True)[:8]

    possible_key_lengths = [
        shift
        for shift, average_ic
        in shifts_and_avg_ic.items()
        if average_ic in highest_avg_ics
    ]

    return possible_key_lengths


# sequence is just the name for part of the cipher text where we take every nth letter
# measures how similar a frequency distribution is to the uniform distribution
def analyze_index_of_coincidence(sequence: str) -> float:

    sequence_letters_and_occurrences = Counter(sequence)
    sequence_letters_occurrences = list(sequence_letters_and_occurrences.values())
    sequence_length = len(sequence)
    sum_of_frequencies = 0.0

    for sequence_letter_occurrence in sequence_letters_occurrences:
        sum_of_frequencies += (sequence_letter_occurrence * (sequence_letter_occurrence - 1))

    index_of_coincidence = (sum_of_frequencies / (sequence_length * (sequence_length - 1)))

    return index_of_coincidence


def get_keyword_length(cipher_text: str) -> List[int]:
    shifts_and_avg_ic = {}

    # starting from 2 till whatever but we'll go for 31 shifts
    for shift in range(2, MAX_SHIFTS):
        average_ic = 0.0

        for _ in range(shift):
            sequence = ''

            for nth in range(0, len(cipher_text), shift):
                if cipher_text[nth].isalpha():
                    sequence += cipher_text[nth]
                else:
                    raise InvalidInput('Sorry, only plain English letters are allowed for now '
                                       '(no special characters or numbers)')

            average_ic += (analyze_index_of_coincidence(sequence) / shift)

        shifts_and_avg_ic.update(
            {
                shift: average_ic,
            }
        )

    possible_key_lengths = analyze_shifts_ic_intervals(shifts_and_avg_ic)

    return possible_key_lengths


def construct_cipher_sequence(starting_index, cipher_text, key_length):
    sequence = ''
    for i in range(starting_index, len(cipher_text), key_length):
        sequence += cipher_text[i]

    return sequence


def analyze_cipher_sequence(sequence: str) -> OrderedD[str, float]:
    letters_and_occurrences = Counter(sequence)
    sum_of_letters_occurrences = 0
    letters_and_frequencies = {}

    for letter_occurrence in letters_and_occurrences.values():
        sum_of_letters_occurrences += letter_occurrence

    for alphabet_letter in ALPHABET_LETTERS_AND_FREQUENCIES.keys():

        if alphabet_letter not in letters_and_occurrences.keys():
            letters_and_frequencies.update(
                {
                    alphabet_letter: 0.0
                }
            )
        else:
            letters_and_frequencies.update(
                {
                    alphabet_letter: round(letters_and_occurrences[alphabet_letter] / sum_of_letters_occurrences, 5)
                }
            )

    sorted_alphabetically = sorted(letters_and_frequencies.items(), key=lambda k: k[0])

    return OrderedDict(sorted_alphabetically)


def shift_list_left(data_list: List[Any]) -> np.ndarray:
    return np.roll(data_list, -1)


def shift_list_right(data_list: List[Any]) -> np.ndarray:
    return np.roll(data_list, 1)


def align_with_alphabet_frequencies(letters_and_frequencies: Dict[str, float]) -> int:
    letters_frequencies = list(letters_and_frequencies.values())
    aligned_frequencies = []

    for shift in range(len(ALPHABET)):

        results = [
            round(letter_frequency * alphabet_letter_frequency, 4)
            for letter_frequency, alphabet_letter_frequency
            in zip(letters_frequencies, ALPHABET_LETTERS_AND_FREQUENCIES.values())
        ]

        aligned_frequencies.append((shift, round(sum(results), 4)))
        letters_frequencies = shift_list_left(letters_frequencies)

    shift = max(aligned_frequencies, key=lambda k: k[1])[0]

    return shift


def perform_frequency_analysis(starting_index: int, cipher_text: str, keyword_length: int) -> int:
    # we know that every 6th letter is encrypted with the same shift amount
    sequence = construct_cipher_sequence(starting_index, cipher_text, keyword_length)
    sequence_letters_and_frequencies = analyze_cipher_sequence(sequence)
    highest_shift = align_with_alphabet_frequencies(sequence_letters_and_frequencies)

    return highest_shift


def generate_possible_keywords(possible_keyword_lengths: List[int], cipher_text: str) -> List[str]:
    possible_keywords = []

    for keyword_length in possible_keyword_lengths:
        keyword = ''

        shift_keys = [
            perform_frequency_analysis(starting_index, cipher_text, keyword_length)
            for starting_index
            in range(keyword_length)
        ]

        for shift_key in shift_keys:
            keyword += ALPHABET[shift_key]

        possible_keywords.append(keyword)

    return possible_keywords


def decrypt(cipher_text: str) -> Tuple[str, str]:
    possible_keyword_lengths = get_keyword_length(cipher_text)
    possible_keywords = generate_possible_keywords(possible_keyword_lengths, cipher_text)

    keywords_and_plain_texts = {}

    for keyword in possible_keywords:
        expanded_keyword = expand_keyword(cipher_text, keyword)
        expanded_shift_keys = calculate_shift_keys(expanded_keyword)

        keywords_and_plain_texts.update(
            {
                keyword: process_text_data(cipher_text, expanded_shift_keys, DECRYPT),
            }
        )

    return find_closest_text_to_english(keywords_and_plain_texts)  # returns the keyword and plain text


def find_closest_text_to_english(keywords_and_plain_texts: Dict[str, str]) -> Tuple[str, str]:
    common_words_count = {}

    for keyword, plain_text in keywords_and_plain_texts.items():
        common_words_found = 0

        for common_word in COMMON_WORDS:
            common_words_found += plain_text.count(common_word)

        if common_words_found in common_words_count.keys():
            # same number of common words have occurred in another keyword combination
            # skip this keyword and favor the first original keyword with the same number of occurrences
            continue

        common_words_count.update(
            {
                common_words_found: [keyword, plain_text]
            }
        )

    keyword, plain_text = common_words_count[sorted(common_words_count.keys(), reverse=True)[0]]

    return keyword, plain_text


if __name__ == '__main__':
    print('*********** Cracking Vigenère Cipher ***********')

    while True:
        try:
            if len(cipher_text_input := input('* Cipher Text: ').upper().replace(' ', '')) > MAX_SHIFTS:
                keyword_output, plain_text_output = decrypt(cipher_text_input)
                formatter = f'* Secret Key: << {keyword_output} >> \n'
                formatter += f'* Plain Text: << {plain_text_output} >> \n'
                formatter += f'******************** \n'

                save_to_file(formatter)
                print(formatter)

            else:
                raise InvalidInput(f'Cipher Text must be more than {MAX_SHIFTS} character')

        except ValueError:
            print('* Choose from available options.\n')

        except InvalidInput as e:
            print(f'* {str(e)}\n')

        except Exception as e:
            print(f'* Something went wrong, kindly report it to me: muhammadamhan@gmail.com')



