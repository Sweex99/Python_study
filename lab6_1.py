#!/usr/bin/env python3

def ui_input() -> list:
    """Input of argument"""
    
    a_side = float(input("Input a side of triangle: "))
    b_side = float(input("Input b side of triangle: "))
    c_side = float(input("Input c side of triangle: "))
    
    return [a_side, b_side, c_side]

def ui_output(result: str) -> None:
    """Output of result"""
    
    result = str(result)
    print("Area of triangle: ", result)

def triangle_area_calculate(sides: list) -> float:
    """Calcucate an return area of sides of triangle"""
    
    if len(sides) > 3 or len(sides) < 3:
        print("Too many or less members of list")
        exit()
    
    p = (sides[0] + sides[1] + sides[2]) / 2
    area = (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5
    
    return area

ui_output(triangle_area_calculate(ui_input()))
