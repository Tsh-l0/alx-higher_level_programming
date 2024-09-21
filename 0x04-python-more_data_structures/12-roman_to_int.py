#!/usr.bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    str_total = 0
    rom_digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for rom in reversed(roman_string):
        rom_digs = rom_digits[rom]
        str_total += rom_digs if str_total < rom_digs * 5 else -rom_digs
    return str_total
