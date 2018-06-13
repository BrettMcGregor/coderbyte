# Challenge
# Using the Python language, have the function AlphabetSoup(str) take the
# str string parameter being passed and return the string with the letters
# in alphabetical order (ie. hello becomes ehllo). Assume numbers and
# punctuation symbols will not be included in the string.
# Sample Test Cases
#
# Input:"coderbyte"
#
# Output:"bcdeeorty"
#
# Input:"hooplah"
#
# Output:"ahhloop"


def alphabet_soup(string):
    return "".join(sorted(string))


print(alphabet_soup("coderbyte"))
print(alphabet_soup("hooplah"))