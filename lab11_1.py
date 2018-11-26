#!/usr/bin/env python3

def parse(filename: str) -> int:
    f = open(filename, 'rt')
    for line in f:
        size = line.split()[9]
        yield int(size)

def output(bytes: list) -> int:
    byte_size = 0
    for byte in bytes:
        byte_size += byte
    print(byte_size)

output(parse("2017_05_07_nginx.txt"))
