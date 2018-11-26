#!/usr/bin/env python3

import decimal

salary = decimal.Decimal(input('Input your salary: '))
person_tax = decimal.Decimal('0.18')
military_tax = decimal.Decimal('0.015')

full_tax = salary * (person_tax + military_tax)

print('You need to pay: ' + str(full_tax))
