#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for inner_mx in matrix:
        print("{:d} {:d} {:d}".format(*inner_mx), end='')
        print()
