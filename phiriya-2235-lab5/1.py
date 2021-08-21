# Phiriya Trakoolwang 633040223-5
"""
Problem 1
"""

import math


def hypotenuse(a, b):
    x = (math.sqrt(math.pow(a, 2) + math.pow(b, 2)))
    print("sqrt({}^2 + {}^2)= {}".format(a, b, x))


hypotenuse(3.0, 4.0)
hypotenuse(3, 4)
hypotenuse(3, 4.0)
