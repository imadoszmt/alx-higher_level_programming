#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list:
        return 0

    counter = 0
    for element in my_list:
        try:
            print("{:}".format(element), end="")
            counter += 1
            if counter >= x:
                break
        except TypeError:
            pass
    print()
    return counter
