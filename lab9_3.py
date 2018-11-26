#!/usr/bin/env python3

def to_Morze(expression: str) -> str:
    morze_val = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-',
    'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
    'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
    'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----'}
    morze_code = [morze_val[_] for _ in ''.join(expression.lower().split())]
    return ''.join(morze_code)

print(to_Morze(input("Input your expression (in English): ")))
