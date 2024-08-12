#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_seq = set(my_list)
    adder = 0
    for element in new_seq:
        adder += element
    return adder
