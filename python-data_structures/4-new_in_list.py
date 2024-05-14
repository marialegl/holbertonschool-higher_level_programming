#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()
    if idx < 0:
        return (copied_list)
    if idx >= len(my_list):
        return (copied_list)
    else:
        modified_list = my_list.copy()
        modified_list[idx] = element
        return modified_list
