"""
Phiriya Trakoolwang, 633040223-5
Lab 2 Problem 1
"""

while True:
    temp_cel = input("Enter a temperature in Celsius: ")
    try:
        temp_cel = float(temp_cel)
        temp_fah = (9 / 5) * temp_cel + 32
        result = round(temp_fah, 2)
        print(f"{round(temp_cel, 2)} in Celsius is {round(result, 2)} Fahrenheit")
    except ValueError:
        print("Please enter a valid floating point for the temperature.")
        continue
    else:
        break
