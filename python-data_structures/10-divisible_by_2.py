#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []  # Lista para almacenar los valores True o False

    # Recorre la lista y verifica si cada elemento es divisible por 2
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
