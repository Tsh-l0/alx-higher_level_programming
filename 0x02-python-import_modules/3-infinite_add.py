#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum_int = 0
    for num in range(len(sys.argv) - 1):
        sum_int += int(sys.argv[num + 1])
    print("{:d}".format(sum_int))
