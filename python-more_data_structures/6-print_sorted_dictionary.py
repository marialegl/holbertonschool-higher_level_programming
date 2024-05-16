#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Ordenar las claves del diccionario alfabéticamente
    sorted_keys = sorted(a_dictionary.keys())

    # Imprimir el diccionario ordenado por las claves
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
