#!/usr/bin/env python3

import decimal

def ui_input() -> list:
    """Input of argument"""
    
    cur_money = decimal.Decimal(input("Input current amount of money: "))
    percent = decimal.Decimal(input("Input annual interest rate of the bank: "))
    duration = decimal.Decimal(input("Input duration in years: "))
    
    return [cur_money, percent, duration]

def ui_output(result: str) -> None:
    """Output of result"""
    
    result = str(result)
    print("Final amount of money: ", result)

def deposit_calculate(deposit_data: list) -> float:
    """Calcucate final amount of money of deposit"""
    
    if len(deposit_data) != 3:
        print("Too many or less members of list")
        exit()
    
    final_money = deposit_data[0] * (1 + deposit_data[1] / 100) ** deposit_data[2]
    
    return final_money

ui_output(deposit_calculate(ui_input()))
