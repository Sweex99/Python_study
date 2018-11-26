#!/usr/bin/env python3

def len_sort(expression: str) -> str:
    return ' '.join(sorted(expression.split(), key=len))

print(len_sort(input("Input your expression: ")))
