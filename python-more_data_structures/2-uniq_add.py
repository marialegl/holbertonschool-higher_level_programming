#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set()
    for x in my_list:
        if isinstance(x, int):
            new_list.add(x)
            return sum(new_list)
