#!/usr/bin/python3

def max_integer(my_list=[]):
    max_num = 0
    if len(my_list) != 0:
        for num in my_list:
            if max_num < num:
                max_num = num
        return max_num
    else:
        return None
