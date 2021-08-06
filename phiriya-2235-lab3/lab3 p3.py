# Phiriya Trakoolwang 633040223-5
"""
Write a program to check whether a character is a vowel or not and if it is,
then convert that character to an uppercase letter and display those uppercase vowels.
Note: use for loop, not list comprehension
"""

vowels = ['A', 'E', 'I', 'O', 'U']
vowels_list = []
input_string = input("Enter a string:")
list_of_letter = list(input_string)
print(f"Characters in the string are {list_of_letter}")
make_it_uppercase = input_string.upper()
for show_only_vowel in make_it_uppercase:
    if show_only_vowel in vowels:
        vowels_list.append(show_only_vowel)
print(f"The entered string is {input_string} and the result of convert a vowel to uppercase is \n {vowels_list}")