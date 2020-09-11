#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    return sum(map(lambda x: int(x[0] * x[1]), my_list)) / sum(map(lambda x: int(x[1]), my_list))
