#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sd = sorted(a_dictionary.items())
    for k, v in sd:
        print('{}: {}'.format(k, v))
