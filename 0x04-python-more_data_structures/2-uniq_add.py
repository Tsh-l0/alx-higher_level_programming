#!/usr/bin/python3

def uniq_add(my_list=[]):
    add2_matrix = 0
    for new_int in set(my_list):
        add2_matrix += new_int
    return add2_matrix
