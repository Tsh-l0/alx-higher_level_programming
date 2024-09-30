#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_new = []
    for el in range(list_length):
        try:
            result_list = my_list_1[el] / my_list_2[el]
        except (ValueError, TypeError):
            print("wrong type")
            result_list = 0
        except ZeroDivisionError:
            print("division by 0")
            result_list = 0
        except IndexError:
            print("out of range")
            result_list = 0
        finally:
            list_new.append(result_list)
    return list_new
