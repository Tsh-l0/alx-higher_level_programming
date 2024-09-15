#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    biggest_int = my_list[0]
    for nums in range(len(my_list)):
        if my_list[nums] > biggest_int:
            biggest_int = my_list[nums]
    return biggest_int
