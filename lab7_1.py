#!/usr/bin/env python3

non_shifted_string = input("Input your string: ")
shifting_number = int(input("Input your number of shift: "))

lfirst = non_shifted_string[0 : shifting_number]
lsecond = non_shifted_string[shifting_number :]
shifted_string = lsecond + lfirst

print(shifted_string)
