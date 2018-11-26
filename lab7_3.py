#!/usr/bin/env python3

expression = input("Input your string: ")
opening = tuple('({[')
closing = tuple(')}]')
mapping = dict(zip(opening, closing))
queue = []

for letter in expression:
    if letter in opening:
        queue.append(mapping[letter])
    elif letter in closing:
        if not queue or letter != queue.pop():
            print(False)
print(not queue)
