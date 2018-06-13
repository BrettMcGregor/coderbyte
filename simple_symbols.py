# Challenge
# Using the Python language, have the function SimpleSymbols(str)
# take the str parameter being passed and determine if it is an
# acceptable sequence by either returning the string true or false.
# The str parameter will be composed of + and = symbols with several
#     letters between them (ie. ++d+===+c++==a) and for the string
#         to be true each letter must be surrounded by a + symbol.
#         So the string to the left would be false. The string will
#         not be empty and will have at least one letter.
# Sample Test Cases
#
# Input:"+d+=3=+s+"
#
# Output:"true"
#
# Input:"f++d+"
#
# Output:"false"


def simple_symbols(string):
    # find index position of alpha save to list
    positions = []
    for char in string:
        if char.isalpha():
            positions.append(string.index(char))
        else:
            continue
    print(positions)
    # search input string either side of alpha characters for '+'
    for pos in positions:
        if pos == 0:
            return False
        elif string[pos - 1] == "+" and string[pos + 1] == "+":
            return True
        return False

print(simple_symbols("+d+=3=+s+"))
print(simple_symbols("f++d+"))
