# Phiriya Trakoolwang 633040223-5
"""
Using enumerate function to display the number (derived from the index)
and the content of the list of fruits = ["Grapefruit", "Longan", "Orange", "Apple", "Cherry"]
uppercase letters and also call the function to sort  fruits
"""


def convert_list():
    global fruits
    i = 1
    variable_fruits = 0
    number = 1
    fruits = ["Grapefruit", "Longan", "Orange", "Apple", "Cherry"]
    print(f"The fruits are {fruits}")
    print("After converting fruits to uppercase letters, fruits are")
    for i in range(len(fruits)):
        fruits[i] = fruits[i].upper()
    for value in fruits:
        print(f"{number}", fruits[variable_fruits])
        i += 1
        number += 1
        variable_fruits += 1
    print("After sorting fruits, fruits are")
    fruits.sort()


if __name__ == "__main__":
    convert_list()
    print(fruits)
