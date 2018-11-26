#!/usr/bin/env python3

import math

a_num = float(input('Input first unsigned number: '))
b_num = float(input('Input second unsigned number: '))

result = (((a_num * b_num) ** 0.5)/(math.exp(a_num) * b_num)) + a_num * math.exp(2 * a_num / b_num)

print('Result: ' + str(result))
