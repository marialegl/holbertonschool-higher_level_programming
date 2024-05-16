#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    ans = 0
    n_len = len(roman_string)
    for (i, v) in enumerate(roman_string):
        if i < n_len - 1 and rom[v] < rom[roman_string[i + 1]]:
            ans -= rom[v]
        else:
            ans += rom[v]
    return ans
