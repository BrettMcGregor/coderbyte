# Challenge
# Using the Python language, have the function LetterChanges(str)
# take the str parameter being passed and modify it using the following
# algorithm. Replace every letter in the string with the letter
# following it in the alphabet (ie. c becomes d, z becomes a).
# Then capitalize every vowel in this new string (a, e, i, o, u)
# and finally return this modified string.
# Sample Test Cases
#
# Input:"hello*3"
#
# Output:"Ifmmp*3"
#
# Input:"fun times!"
#
# Output:"gvO Ujnft!"


def letter_changes(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    new_string = []
    for char in string:
        if char.isalpha():
            if char == "z":
                new_string.append("a")
            elif alphabet[alphabet.find(char) + 1] in vowels:
                new_string.append((alphabet[alphabet.find(char) + 1]).upper())
            else:
                new_string.append(alphabet[alphabet.find(char) + 1])
        else:
            new_string.append(char)
    return "".join(new_string)


print(letter_changes("hello * 3"))
print(letter_changes("fun times!"))
