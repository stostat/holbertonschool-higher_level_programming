#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = dict(filter(lambda elem: elem[1] == value, a_dictionary.values()))
    return new_dict
