#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for inner_mx in matrix:
        for element in inner_mx:
            print(element, end=' ')
        print()
