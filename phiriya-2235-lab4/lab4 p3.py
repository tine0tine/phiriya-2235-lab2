# Phiriya Trakoolwang 633040223-5
"""
Write a program to compute the covid19stats difference between today and yesterday
"""


def get_float(arg):
    correct_input = False
    while not correct_input:  # this is a while loop
        try:
            number = float(input(f"Enter the number of new infected Covid19 cases for {arg}:"))
            return number
        except ValueError:
            print("Please enter a valid integer \nStay healthy!")


def add():
    numberOfYesterday = get_float("yesterday")
    numberOfToday = get_float("today")
    x = (numberOfYesterday-numberOfToday)/numberOfYesterday
    percentage = f"{x:.0%}"
    print(percentage)

    # if operator == "+":
    #     answer_plus = n1 + n2
    #     print(f'The answer of {n1} + {n2} is {answer_plus}')
    # elif operator == "-":
    #     answer_negative = n1 - n2
    #     print(f'The answer of {n1} - {n2} is {answer_negative}')
    # elif operator == "*":
    #     answer_time = n1 * n2
    #     print(f'The answer of {n1} * {n2} is {answer_time}')
    # elif operator == "/":
    #     if n2 == 0:
    #         print("Cannot divide by zero")
    #     else:
    #         answer_divide = n1 / n2
    #         print(f'The answer of {n1} / {n2} is {answer_divide}')
    # else:
    #     print("Unknown operator")


if __name__ == "__main__":
    add()
