# Challenge
# Using the Python language, have the function CheckNums(num1,num2)
# take both parameters being passed and return the string true if num2
# is greater than num1, otherwise return the string false. If the
# parameter values are equal to each other then return the string -1.
# Sample Test Cases
#
# Input:3 & num2 = 122
#
# Output:"true"
#
# Input:67 & num2 = 67
#
# Output:"-1"


def check_nums(num1, num2):
    if num2 > num1:
        return 'true'
    elif num2 == num1:
        return '-1'
    return 'false'


print(check_nums(3, 122))
print(check_nums(67, 67))