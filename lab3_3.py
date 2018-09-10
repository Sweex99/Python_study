#!/usr/bin/env python3

height = input('Введіть зріст (метрах): ')
weight = input('Введіть вагу (kg): ')

index = float(weight) / float(height) ** 2

print('Ваш індекс: ' + str(index))
