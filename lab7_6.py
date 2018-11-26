#!/usr/bin/env python3

def frame_output(expression: str) -> None:
    print('*' * len(expression) + "****")
    print("*", expression, "*")
    print('*' * len(expression) + "****")

frame_output(input("Input your string: "))
