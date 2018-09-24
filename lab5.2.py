#!/usr/bin/env python3

height = int(input("Enter height: "))
width = int(input("Enter width: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if height > a and width > b:
    print("Success")
elif height > a and width > c:
    print("Success")
elif height > b and width > c:
    print("Success")
if height > b and width > a:
    print("Success")
elif height > c and width > a:
    print("Success")
elif height > c and width > b:
print("Success")
else:
print("Failure")
