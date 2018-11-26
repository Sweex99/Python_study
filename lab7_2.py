#!/usr/bin/env python3

string = input("Input your string: ")
string = ''.join(e for e in string if e.isalnum()).lower()
reverse_string = string[::-1]

print(string == reverse_string)
