#!/usr/bin/python3

def best_score(a_dictionary):
    biggest_value = 0
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            if biggest_value <= value:
                biggest_value = a_dictionary[key]
            val = biggest_value
        for key, value in a_dictionary.items():
            if value == val:
                return key
    return None


