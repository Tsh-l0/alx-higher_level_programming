#!/usr/bin/python3
for d_digits in range(100):
    if d_digits < 99:
        print("{:02d}, ".format(d_digits), end="")
    else:
        print("{:02d}".format(d_digits))
