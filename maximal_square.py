# Challenge - HARD
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
    """
    To find the largest sub-matrix comprised completely of 1's we will set up search
    coordinates and complete a search for each cell using these 'neighbour' coordinates

    :param args: matrix contents
    :return: area of largest sub-matrix of 1's
    """
    array = [arg for arg in args]  # parse string to array
    print(f"{'array':-^9}")
    for item in array:
        print(" ".join(item))
    print()
    # generate the search matrix

    # TODO not sure about this size variable.
    # need to start by searching for a submatrix = size of matrix
    # then to reduce the submatrix search size each iteration until
    # max submatrix size is found
    # need to deal with the case of non-square matrix/array
    size = min(len(array), len(array[0]))

    while True:
        area = 0
        search = []

        if area > 0:
            return area
        else:
            for i in range(size):
                for j in range(size):
                    search.append((i, j))
            print(f"search = {search}")  # coordinates of search area/cells
            print()
            print("*" * 60)
            print(f"size = {size}")
            # start searching from each cell starting at top left [0][0]
            for row in range(len(array) - size + 1):
                # print(f"row {row} = {array[row]}")  # TODO delete line
                for cell in range(len(array[row]) - size + 1):
                    local = []
                    for neighbour in search:
                        print(f"search for row {row} cell {cell} is {row + neighbour[0], cell + neighbour[1]} "
                              f"returns {array[row + neighbour[0]][cell + neighbour[1]]}")
                        local.append(array[row + neighbour[0]][cell + neighbour[1]])
                    print()
                    print(f"local = {local}")  # this is the contents of the searched cells TODO delete line
                    print()
                    if all(x == "1" for x in local):
                        area = size * size
                        return f"Area = {area}"
            size -= 1

# print(maximal_square("101", "011", "011", "101"))  # 4: rectangular matrix
# print(maximal_square("111", "111", "111"))  # 9
# print(maximal_square("1111", "1111", "1111", "1111"))  # 16
# print(maximal_square("0111", "1111", "1111", "1111"))  # 9
# print(maximal_square("0111", "1101", "0111"))  # 1
print(maximal_square("10110", "11101", "11110", "11110", "01011"))  # 9
