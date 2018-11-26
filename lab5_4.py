#!/usr/bin/env python3

import math

a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

if a == 0 and b != 0:
    x1 = x2 = -(c / b)
elif a == 0 and b == 0:
    x1 = x2 = Any
else:
    discriminant = b ** 2 - 4 * a * c
    x1 = (-b + discriminant ** 0.5)/2 * a
    x2 = (-b - discriminant ** 0.5)/2 * a
print("x1=" + str(x1) + "\t" + "x2=" + str(x2))
