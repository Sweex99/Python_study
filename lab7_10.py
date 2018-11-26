#!/usr/bin/env python3

def get_smallest(expression: str) -> str:
    return min(expression.split())

print(get_smallest(input("Input your expression: ")))
