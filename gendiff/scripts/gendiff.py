#!usr/bin/env python3

import argparse
from gendiff.parsers import parsers


def generate_diff(f1, f2):

    if len(f1) == 0 and len(f2) == 0:
        return
    else:

        files = parsers.parsed_files(f1, f2)
        file1 = files[0]
        file2 = files[1]

        dict1 = {y: x for x, y in file1.items()}
        dict2 = {y: x for x, y in file2.items()}

        dict_temp = dict()
        dict_temp.update(dict1)
        dict_temp.update(dict2)
        dict_temp_sorted = sorted(dict_temp, key=dict_temp.get)

        dict_result = {}

        for w in dict_temp_sorted:
            dict_result[w] = dict_temp[w]

        result_str = '{\n'

        for k, v in dict_result.items():

            result_str += '  '

            if dict1.get(k) and not dict2.get(k):
                result_str += '- '
            if dict1.get(k) and dict2.get(k):
                result_str += '  '
            if dict2.get(k) and not dict1.get(k):
                result_str += '+ '

            result_str += f'{v}: {k}\n'

        result_str += '}'

    return result_str


def main():

    desc = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('file_1', metavar='first_file')
    parser.add_argument('file_2', metavar='second_file')

    args = parser.parse_args()

    result = generate_diff(args.file_1, args.file_2)
    print(result)


if __name__ == '__main__':
    main()
