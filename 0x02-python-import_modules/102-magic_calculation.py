#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(num1, num2):
    if num1 < num2:
        num3 = add(num1, num2)
        for i in range(4, 6):
            num3 = add(num3, i)
        return num3
    return sub(num1, num2)
