# Phiriya Trakoolwang 633040223-5
"""
Problem 2
"""

import math


def hypotenuse(num1, num2):
    try:
        if not num1:
            raise ValueError
        x = math.sqrt.pow(num1, 2) + math.pow(num2, 2)
        return x
    except Exception:
        pass


print(f"hypotenuse(3,4) is {hypotenuse(3.0, 4.0)}")
print(f"hypotenuse('3','4') is {hypotenuse('3', '4')}")
print(f"hypotenuse(3,'4') is {hypotenuse(3, '4.0')}")
