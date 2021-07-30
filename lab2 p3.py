"""
Phiriya Trakoolwang, 633040223-5
Lab 2 Problem 3
"""

list = [1, 2, 3, 4, 5]


def add_number_to_list():
    global list1
    print("Before adding an integer, the list is ", list1)
    add_list = int(input("Enter a number to add to a list: "))
    list1.append(add_list)
    print("After adding an integer", add_list, ", the list is", list1)


def replace():
    global replace_list, find_list
    print("Finding a number to replace in the list", list1)
    find_list = int, input("Enter a number to find: ")
    replace_list = int, input("Enter a new number to replace: ")
    list1.remove()
    list1.append(replace_list)
    print("After replacing", find_list, "with", replace_list, ", the new list is", list1)


def remove_number_in_list():
    list1.remove(replace_list)
    list1.append(find_list)
    print("Finding a number to remove in the list", list1)
    remove_list = int, input("Enter a number to remove: ")
    list1.remove(remove_list)
    print("After removing", remove_list, ", the list is", list1)


if __name__ == '__main__':
    add_number_to_list()
    replace_number_in_list()
    remove_number_in_list()
