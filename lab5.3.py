#!/usr/bin/env python3

import random

user_instrument = int(input("Choose your instrument\n1.Rock\n2.Paper\n3.Scissor$

script_instrument = random.randrange(1, 4)

if user_instrument == 1 and script_instrument == 2:
    print("It\'s paper\nScript Win!!!")
elif user_instrument == 2 and script_instrument == 3:
    print("It\'s scissors\nScript Win!!!")
elif user_instrument == 3 and script_instrument == 1:
    print("It\'s rock\nScript Win!!!")
elif user_instrument == 2 and script_instrument == 1:
    print("It\'s rock\nUser Win!!!")
elif user_instrument == 3 and script_instrument == 2:
    print("It\'s paper\nUser Win!!!")
elif user_instrument == 1 and script_instrument == 3:
    print("It\'s scissors\nUser Win!!!")
else:
    print("Draw")
    if script_instrument == 1:
        print("It\'s rock")
    elif script_instrument == 2:
        print("It\'s paper")
    elif script_instrument == 3:
        print("It\'s scissors")
else: pass
