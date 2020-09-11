#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num_sum = 0
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    for i in range(len(roman_string)):
        if i + 1 >= len(roman_string):
            num_sum += roman_dic[roman_string[i]]
            break
        if roman_dic[roman_string[i]] < roman_dic[roman_string[i + 1]]:
            num_sum -= roman_dic[roman_string[i]]
        else:
            num_sum += roman_dic[roman_string[i]]
    return num_sum
