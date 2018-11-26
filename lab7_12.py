#!/usr/bin/env python3

def del_whitespaces(expression: str) -> str:
    return ' '.join(expression.split())

print(del_whitespaces(input("Input your expression: ")))
