#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for inner_matrix in matrix:
        squared_inner_matrix = list(map(lambda x : x**2, inner_matrix))
        squared_matrix.append(squared_inner_matrix)
    return squared_matrix 
