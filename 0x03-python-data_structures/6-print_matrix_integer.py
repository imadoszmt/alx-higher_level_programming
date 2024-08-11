#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for inner_mx in matrix:
        for index, element in enumerate(inner_mx):
            print("{:d}".format(element), end='')

            if index < len(inner_mx) - 1:
                print(" ", end='')

        print()
