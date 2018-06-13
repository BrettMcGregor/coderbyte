# Challenge
# Using the Python language, have the function LetterCapitalize(str)
# take the str parameter being passed and capitalize the first letter
# of each word. Words will be separated by only one space.
# Sample Test Cases
#
# Input:"hello world"
#
# Output:"Hello World"
#
# Input:"i ran there"
#
# Output:"I Ran There"


def letter_capitalise(string):
    return " ".join(x.capitalize() for x in string.split())


print(letter_capitalise("hello world"))
print(letter_capitalise("i ran there"))