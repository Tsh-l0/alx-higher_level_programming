#!/usr/bin/python3
"""
A function that prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """
    Args:
        test: The text to be printed. Must be str

    TypeError:
        If test is not str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    txt_flag = 0
    while txt_flag < len(text) and text[txt_flag] == " ":
        txt_flag = txt_flag + 1

    while txt_flag < len(text):
        print(text[txt_flag], end="")
        if text[txt_flag] == "\n" or text[txt_flag] in ".?:":
            if text[txt_flag] in ".?:":
                print("\n")
            txt_flag = txt_flag + 1
            while txt_flag < len(text) and text[txt_flag] == " ":
                txt_flag = txt_flag + 1
            continue
        txt_flag = txt_flag + 1
