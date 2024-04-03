#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for element in my_list:
        try:
            print("{:}".format(element), end="")
            counter += 1
            if counter >= x or not my_list[counter]:
                break
        except IndexError:
            break
    print()
    return counter or 0
