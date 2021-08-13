# Phiriya Trakoolwang 633040223-5
"""
Problem 2 (2 points) Develop a program that accept two floating point numbers and then perform arithmetic operations according to the given operator (+, -, *, /)
The program will implement only one function (hint: you can use arguments to handle two different inputs) to keep asking a correct formatted operand until the user enters a valid floating point number (using try and except block)
The program will check whether the divisor is zero or not (using try and except block)
Note: please look at adder.py to see how you can define one function to get two inputs
"""


def get_float(arg):
    correct_input = False
    while not correct_input:  # this is a while loop
        try:
            number = float(input(f"Enter {arg} floating point number:"))
            return number
        except ValueError:
            print("Please enter a valid floating point number")


def add():
    n1 = get_float("the first")
    n2 = get_float("the second")

    operator_list = [["+"], ["-"], ["*"], ["/"]]
    operator = input("Please enter an operator (+,-,*,/):")
    if operator == "+":
        answer_plus = n1 + n2
        print(f'The answer of {n1} + {n2} is {answer_plus}')
    elif operator == "-":
        answer_negative = n1 - n2
        print(f'The answer of {n1} - {n2} is {answer_negative}')
    elif operator == "*":
        answer_time = n1 * n2
        print(f'The answer of {n1} * {n2} is {answer_time}')
    elif operator == "/":
        if n2 == 0:
            print("Cannot divide by zero")
        else:
            answer_divide = n1 / n2
            print(f'The answer of {n1} / {n2} is {answer_divide}')
    else:
        print("Unknown operator")


if __name__ == "__main__":
    add()
