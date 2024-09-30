#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    e_count = 0
    for e in range (x):
        try:
            print(f"{my_list[e]}", end="")
            e_count += 1
        except IndexError:
            break
    print()
    return (e_count)
