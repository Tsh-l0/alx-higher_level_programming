#!/usr/bin/python3

if __name__ == "__main__":
    import sys 

    arg_count = len(sys.argv) - 1

    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument: ")
    else:
        print("{} arguments:".format(arg_count))

    for arguments in range(1, arg_count + 1):
        print("{}: {}".format(arguments, sys.argv[arguments]))
