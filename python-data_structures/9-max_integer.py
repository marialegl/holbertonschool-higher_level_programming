#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == 0:
        return (None)
    # Suponemos que el primer elemento es el máximo inicialmente
    maximo = my_list[0]
    for element in my_list:
        if element > maximo:
            maximo = element
    return maximo
