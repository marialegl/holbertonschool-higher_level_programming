#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    num = len(matrix)
    num_expo = len(matrix[0]) if matrix else 0

    squared_matrix = [[0] * num_expo for _ in range(num)]

    for i in range(num):
        for j in range(num_expo):
            squared_matrix[i][j] = matrix[i][j] ** 2

    return squared_matrix
