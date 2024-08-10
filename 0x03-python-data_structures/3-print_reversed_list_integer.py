#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list) - 1
    for num in my_list:
        print("{}".format(my_list[list_len]))
        list_len -= 1
