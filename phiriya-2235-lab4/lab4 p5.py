# Phiriya Trakoolwang 633040223-5
"""
Problem 5
"""

import logging

inputLogging = False

while not inputLogging:
    try:
        n1 = int, input("Enter n1:")
        n2 = int, input("Enter n2:")
        if n2 < 0:
            break
        result = n1 / n2
        print(f"The result is {result}")
        logging.debug(f"")