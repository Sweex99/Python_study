#!/usr/bin/env python3

def is_lucky_ticket(expression: str) -> bool:
    halfing_number = int(len(expression) / 2)
    first_half = list(map(int, expression[0 : halfing_number]))
    second_half = list(map(int, expression[-halfing_number :]))
    return sum(first_half) == sum(second_half)

print(is_lucky_ticket(input("Input your ticket number: ")))
