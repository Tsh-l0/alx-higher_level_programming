#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for dict_keys in sorted(a_dictionary.keys()):
        print('{}: {}'.format(dict_keys, a_dictionary[dict_keys]))
