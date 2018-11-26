#!/usr/bin/env python3

import random

def gen_list(size: int) -> list:
    return [random.randint(0, 10) for _ in range(size)]

def selection_sort(source: list) -> list:
    for i in range(len(source)):
        min_i = min(source[i:])
        min_index = source[i:].index(min_i)
        source[i + min_index] = source[i]
        source[i] = min_i
    return source

lst = gen_list(10)
print(lst)
print(selection_sort(lst))
