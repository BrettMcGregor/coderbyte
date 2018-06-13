# Challenge Using the Python language,
# Have the function PentagonalNumber(num) read num which will be a positive
# integer and determine how many dots exist in a pentagonal shape around
# a center dot on the Nth iteration.
#  For example, in the image below you can see that on the first iteration
# there is only a single dot, on the second iteration there are 6 dots, on
# the third there are 16 dots, and on the fourth there are 31 dots.
# Your program should return the number of dots that exist in the whole
# pentagon on the Nth iteration.
#     Sample Test Cases
#
# Input:2
#
# Output:6
#
# Input:5
#
# Output:51


def pentagonal_number(num):  # num = number of iterations growing a pentagon by adding dots
    dots = [1]
    for i in range(1, num):
        dots.append(5 * i)
    return sum(x for x in dots)



print(pentagonal_number(1))  # 1
print(pentagonal_number(2))  # 6
print(pentagonal_number(3))  # 16
print(pentagonal_number(4))  # 31 dots
print(pentagonal_number(8))  # 51 dots
