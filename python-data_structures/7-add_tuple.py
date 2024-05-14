#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Si la tupla a tiene menos de 2 elementos, añade ceros para completarla
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    else:
        # Si la tupla a tiene más de 2 elementos, toma solo los primeros 2
        tuple_a = tuple_a[:2]

    # Si la tupla b tiene menos de 2 elementos, añade ceros para completarla
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
    else:
        # Si la tupla b tiene más de 2 elementos, toma solo los primeros 2
        tuple_b = tuple_b[:2]

    # Suma los primeros dos elementos de cada tupla
    sum_first = tuple_a[0] + tuple_b[0]
    sum_second = tuple_a[1] + tuple_b[1]

    # Retorna una nueva tupla con la suma de los elementos
    return (sum_first, sum_second)
