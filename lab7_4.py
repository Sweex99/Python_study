#!/usr/bin/env python3

def caesar(expression: str) -> str:
    lst = list(map(lambda x: chr(ord(x) + 1), expression))
    return ''.join(lst)

print(caesar(input("Input your string: ")))
