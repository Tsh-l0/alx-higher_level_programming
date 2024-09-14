#1/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_len1 = len(tuple_a)
    tuple_len2 = len(tuple_b)

    if tuple_len1 < 2:
        tuple_a += (0, 0)

    if tuple_len2 < 2:
        tuple_b += (0, 0)

    mod_tuple = tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1]
    return mod_tuple
