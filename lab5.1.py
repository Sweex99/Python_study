#!/usr/bin/env python3

s = input("Input positive number: ")
a = int(s)


#print(str(modify_s))
print(a != 0 and ((a & (a - 1)) == 0))
