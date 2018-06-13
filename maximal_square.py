# Challenge
# Using the Python language, have the function MaximalSquare(strArr) take the
# strArr parameter being passed which will be a 2D matrix of 0 and 1's, and
# determine the area of the largest square submatrix that contains all 1's.
# A square submatrix is one of equal width and height, and your program should
# return the area of the largest submatrix that contains only 1's. For example:
# if strArr is ["10100", "10111", "11111", "10010"] then this looks like the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# For the input above, you can see the bolded 1's create the largest square
# submatrix of size 2x2, so your program should return the area which is 4.
# You can assume the input will not be empty.
#
# Hard challenges are worth 15 points and you are not timed for them.
#     Sample Test Cases
#
# Input:"0111", "1111", "1111", "1111"
#
# Output:9
#
# Input:"0111", "1101", "0111"
#
# Output:1


def maximal_square(*args):
    # parse string to array
    array = [arg for arg in args]
    # return array
# complete search for each cell looking clockwise from search cell

# generate search matrix
    search = []
    size = 3
    for i in range(size):
        for j in range(size):
            search.append((i, j))
    # print(search)
    # start top left [0][0]
    for item in array:
        print(" ".join(item))
    area = 0

    print(f"search = {search}")  # coordinates of search area/cells
    for row in range(len(array) - size + 1):
        # print(f"row {row} = {array[row]}")
        for cell in range(len(array) - size + 1):
            # print(f"cell {cell} = {array[row][cell]}")
            local = []
            for neighbour in search:
                # print(f"search for row {row} cell {cell} is {row + neighbour[0], cell + neighbour[1]} "
                #       f"returns {array[row + neighbour[0]][cell + neighbour[1]]}")
                local.append(array[row + neighbour[0]][cell + neighbour[1]])
            # print(local) # this is the contents of the searched cells
            if all(x == "1" for x in local):
                print(size)
                area = size * size
    return area


print(maximal_square("0111", "1111", "1111", "1111"))
# print(maximal_square("0111", "1101", "0111"))

