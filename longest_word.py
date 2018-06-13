# Using the Python language, have the function
# LongestWord(sen) take the sen parameter being
# passed and return the largest word in the string.
# If there are two or more words that are the same
# length, return the first word from the string with
# that length. Ignore punctuation and assume sen will not be empty.

#
# Input:"fun&!! time"
#
# Output:"time"
#
# Input:"I love dogs"
#
# Output:"love"


def longest_word(sen):
    clean_string = ""
    for char in sen:
        if char.isalpha() or char == " ":
            clean_string = clean_string + char
        else:
            continue
    words = clean_string.split()
    length = 0
    longest = ""
    for word in words:
        if len(word) > length:
            longest = word
            length = len(word)
    return longest


print(longest_word("fun&!! time"))
print(longest_word("I love dogs"))
