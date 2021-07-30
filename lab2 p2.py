"""
Phiriya Trakoolwang, 633040223-5
Lab 2 Problem 2
"""


def input_midterm_mark():
    while True:
        midterm_mark = input("Please enter the student's midterm exam mark (0-100): ")
        try:
            midterm_mark = float(midterm_mark)
        except ValueError:
            print("Please enter a score as a decimal number")
            continue
        if 100 < midterm_mark or 0 > midterm_mark:
            print("Please enter a score in the range [0,100]")
            continue
        else:
            return midterm_mark


def input_final_mark():
    while True:
        final_mark = input("Please enter the student's final exam mark (0-100): ")
        try:
            final_mark = float(final_mark)
        except ValueError:
            print("Please enter a score as a decimal number")
            continue
        if 0 > final_mark or 100 < final_mark:
            print("Please enter a score in the range [0,100]")
            continue
        else:
            return final_mark


def grader_and_display():
    std_id = input("Please enter your student ID: ")

    transfer_score = (asking_std_midterm_mark * 0.4) + (asking_std_final_mark * 0.6)
    transfer_score = float(transfer_score)

    if 80 <= transfer_score <= 100:
        grade = "A"
    elif 70 <= transfer_score < 80:
        grade = "B"
    elif 60 <= transfer_score < 70:
        grade = "C"
    elif 50 <= transfer_score < 60:
        grade = "D"
    else:
        grade = "F"

    print("Student ID", std_id, "has the total mark as", transfer_score, "and has grade as", grade)


if name == 'main':
    grader_and_display()
