#!/usr/bin/env python3

def get_fizzbuzz() -> str:
    return [(not n % 3) * 'Fizz' + (not n % 5) * 'Buzz' or n for n in range(1, 101)]

print(get_fizzbuzz())
