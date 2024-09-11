#!/usr/bin/python3
def fizzbuzz():
    for int in range(1, 101):
        if int % 3 == 0 and int % 5 == 0:
            print("FizzBuzz ", end="")
        elif int % 3 == 0:
            print("Fizz ", end="")
        elif int % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(int), end="")
