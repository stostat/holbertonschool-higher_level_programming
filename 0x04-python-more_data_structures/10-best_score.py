#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        n = sorted(a_dictionary.values())[-1]
        for key, value in a_dictionary.items(): 
            if n == value:
                return key
