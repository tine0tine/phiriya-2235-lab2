"""
Phiriya Trakoolwang, 633040223-5
Lab 2 Problem 4
"""

str_intput = str(input("Enter string input: "))
vowels = "AEIOUaeiou"


def check_vowels(string, vowels):
    result = [each for each in string if each in vowels]
    print(f"Vowels in {str_intput} are {result}")


check_vowels(str_intput, vowels)
