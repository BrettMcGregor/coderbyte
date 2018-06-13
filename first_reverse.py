# Challenge
# Using the Python language, have the function FirstReverse(str)
# take the str parameter being passed and return the string in reversed order.
# For example: if the input string is "Hello World and Coders" then your
# program should return the string sredoC dna dlroW olleH.
# Sample Test Cases
#
# Input:"coderbyte"
#
# Output:"etybredoc"
#
# Input:"I Love Code"
#
# Output:"edoC evoL I"


def first_reverse(string):
    return string[-1::-1]


print(first_reverse("Hello World and Coders"))
