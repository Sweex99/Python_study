#!/usr/bin/env python3

import decimal
import math

def ui_input() -> list:
    """Input of argument"""
    
    cur_money = decimal.Decimal(input("Input current amount of money: "))
    percent = decimal.Decimal(input("Input annual interest rate of the bank: "))
    final_money = decimal.Decimal(input("Input final amount of money: "))
    
    return [cur_money, percent, final_money]

def ui_output(result: str) -> None:
    """Output of result"""
    
    result = str(result)
    print("Duration of deposit: ", result)

def deposit_duration_calculate(deposit_data: list) -> float:
    """Calcucate duration of deposit"""
    
    if len(deposit_data) != 3:
        print("Too many or less members of list")
        exit()
    
    #TODO duration
    duration = math.log(deposit_data[2] / deposit_data[0], (1 + deposit_data[1] / 100))
    
    return duration

ui_output(deposit_duration_calculate(ui_input()))
