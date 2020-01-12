import os
from constants import ROOT_DIR, RESULTS_DIR_NAME, RESULTS_FILENAME

RESULTS_DIR = os.path.join(ROOT_DIR, RESULTS_DIR_NAME)


def save_to_file(data: str, filename: str = RESULTS_FILENAME):
    results_filename = f'{filename}.txt'
    operation = 'w'
    results_dir = os.path.join(RESULTS_DIR, results_filename)

    os.makedirs(RESULTS_DIR, exist_ok=True)

    while os.path.exists(results_dir):
        if (operation := str(input(f'File "{results_dir}" already exists, would you like to: \n'
                                   '* append (a)\n'
                                   '* overwrite (w)\n'
                                   '* cancel (c)\n'
                                   '-> ')).lower()) in ['a', 'w']:

            with open(results_dir, operation) as file_handler:
                file_handler.writelines(data)
                break

        elif operation == 'c':
            print('Operation cancelled')
            break

        else:
            print(f'Invalid mode: "{operation}" please specify whether to append or overwrite.')
    else:

        try:
            with open(results_dir, operation) as file_handler:
                file_handler.writelines(data)

            print(f'* File created with the decrypted text at "{results_dir}". \n')

        except FileNotFoundError:
            pass
