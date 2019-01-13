#!/usr/bin/env python3

import timeit

for_time = timeit.timeit('lab17_2.revers_all_by_for(lst)', \
        setup='import lab17_2; \
        lst = [ \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        ]',
        number=100000)
comp_time = timeit.timeit('lab17_2.revers_all_by_comprehension(lst)', \
        setup='import lab17_2; \
        lst = [ \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        ]',
        number=100000)
map_time = timeit.timeit('lab17_2.revers_all_by_map(lst)', \
        setup='import lab17_2; \
        lst = [ \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        "123", "abc", "qwerty", "123", "abc", "qwerty", \
        ]',
        number=100000)

shift_time = timeit.timeit('lab17_2.power_by_shift()', \
        setup='import lab17_2', \
        number=100000)

double_star_time = timeit.timeit('lab17_2.power_by_double_star()', \
        setup='import lab17_2', \
        number=100000)

pow_time = timeit.timeit('lab17_2.power_by_pow()', \
        setup='import lab17_2', \
        number=100000)

math_pow_time = timeit.timeit('lab17_2.power_by_math_pow()', \
        setup='import lab17_2', \
        number=100000)

print("For time is", for_time)
print("Comprehension time is", comp_time)
print("Map time is", map_time)
print("Shift time is", shift_time)
print("Double star time is", double_star_time)
print("Pow time is", pow_time)
print("Math.pow time is", math_pow_time)
