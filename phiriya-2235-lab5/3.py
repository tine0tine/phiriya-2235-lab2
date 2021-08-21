# Phiriya Trakoolwang 633040223-5
"""
Problem 3
"""


def recursive(n):
    if n == 1:
        return n
    else:
        return n * recursive(n - 1)


while True:
    try:

        n = int(input("Enter a non-negative integer:"))
        if n < 0:
            print("Please enter an integer that is non-negative")
            break
        elif n == 0:
            print("The factorial of 0 is 1")
        else:
            print(f"The factorial of {n} is {recursive(n)}")

    except ValueError:
        print("Please enter a valid integer")
        break
