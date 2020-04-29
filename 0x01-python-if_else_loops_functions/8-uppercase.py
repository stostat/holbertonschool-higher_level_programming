#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            to_up = 32
        else:
            to_up = 0
        print("{:c}".format(ord(i) - to_up), end="")
    print()
