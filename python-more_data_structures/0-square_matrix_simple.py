#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_square = []
    # Iterar sobre cada fila de la matriz
    for file in matrix:
        # Crear una nueva fila para los cuadrados
        file_square = []
        # Iterar sobre cada elemento de la fila
        for element in file:
            # Calcular el cuadrado del elemento y añadirlo a la nueva fila
            file_square.append(element ** 2)
            # Añadir la nueva fila a la matriz de cuadrados
        matrix_square.append(file_square)
    return (matrix_square)
