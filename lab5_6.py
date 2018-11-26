#!/usr/bin/env python3

first_len = int(input("Input first length: "))
second_len = int(input("Input second length: "))
third_len = int(input("Input third length: "))

hypotenuse = max(first_len, second_len, third_len)
cathetes_sum = (first_len + second_len + third_len) - hypotenuse

if first_len <= 0 or second_len <= 0 or third_len <= 0:
    print("Triangle does not exist")
elif cathetes_sum > hypotenuse:
    print("Triangle exists")
else:
    print("Triangle does not exist")
