# Challenge
# Using the Python language, have the function KaprekarsConstant(num)
# take the num parameter being passed which will be a 4-digit number
# with at least two distinct digits. Your program should perform the
# following routine on the number: Arrange the digits in descending
# order and in ascending order (adding zeroes to fit it to a 4-digit
# number), and subtract the smaller number from the bigger number.
# Then repeat the previous step. Performing this routine will always
# cause you to reach a fixed number: 6174. Then performing the routine
# on 6174 will always give you 6174 (7641 - 1467 = 6174). Your program
# should return the number of times this routine must be performed until
# 6174 is reached. For example: if num is 3524 your program should return
# 3 because of the following steps: (1) 5432 - 2345 = 3087,
# (2) 8730 - 0378 = 8352, (3) 8532 - 2358 = 6174.
#
# Hard challenges are worth 15 points and you are not timed for them.
#     Sample Test Cases
#
# Input:2111
#
# Output:5
#
# Input:9831
#
# Output:7


def kaprekars_constant(num):
    kc = num
    counter = 0
    while True:
        if kc == 6174:
            return counter
        else:
            counter += 1
            num_a = int("".join(sorted(str(kc))))
            # arrange in descending order (keep leading zeros)
            num_d = int("".join(sorted(str(kc).zfill(4), reverse=True)))
            # subrct smaller from larger
            kc = num_d - num_a


print(kaprekars_constant(9831))
