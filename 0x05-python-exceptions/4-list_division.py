#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        new_list = list(map(lambda x, y: x / y, my_list_1, my_list_2))
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return new_list
