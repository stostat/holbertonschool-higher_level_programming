#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        n = sorted(a_dictionary.values())[-1]
        for key, value in a_dictionary.items():
            if n == value:
                return key
