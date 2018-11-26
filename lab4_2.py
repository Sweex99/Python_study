#!/usr/bin/env python3

import math

a_num = float(input('Input first real number: '))
b_num = float(input('Input second real number: '))
c_num = float(input('Input third real number: '))

result = (1 / (c_num * (2 * math.pi) ** 0.5)) * math.exp(-(a_num - b_num) ** 2 /
2 * c_num ** 2)

print('Result: ' + str(result))
