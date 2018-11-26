#!/usr/bin/env python3

expression = input("Input your string (in English): ")

count = expression.count('a') + expression.count('o') + \
expression.count('u') + expression.count('i') + expression.count('e') \
+ expression.count("y")

print(count)
