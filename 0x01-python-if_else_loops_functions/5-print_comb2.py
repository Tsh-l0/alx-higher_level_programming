#!/usr/bin/python3
for d_digits in range(100):
    if d_digits < 99:
        print(f"{d_digits:02d}, ", end="") #Print nos with 2 digits + ','
    else:
        print(f"{d_digits:02d}") #Print last number + newline
