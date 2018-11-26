#!/usr/bin/env python3

height = input('Input your height in m: ')
weight = input('Input your weight in kg: ')

index = float(weight) / float(height) ** 2

print('Your Body Mass Index: ' + str(index))
