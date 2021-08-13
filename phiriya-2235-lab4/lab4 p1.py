# Phiriya Trakoolwang 633040223-5
"""
Given with prob1-bug.py as shown in Figure 1, modify the code and save the new file as prob1-sol.py such that it gives the correct output as shown in Figure 2.
"""

patients = [[70, 1.80], [58, 1.55], [100, 1.90]]


def calculate_bmi(_weight, _height):
    return _weight / (_height ** 2)


case_list = 0
for patient in range(1, 4):
    weight, height = patients[case_list]
    bmi = calculate_bmi(weight, height)
    case_list += 1
    print(f"Patient's BMI is: {bmi:0.02f}")
