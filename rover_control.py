# VISA internship for bachelor question.
# Complete the 'roverMove' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER matrixSize
#  2. STRING_ARRAY cmds


def roverMove(matrixSize, cmds):
    # Write your code here

    matrix = []
    count = 0
    for i in range(matrixSize * matrixSize):
        matrix.append(i)
    print(matrix)
    start_point_value = matrix[0]
    previous_point_value = matrix[0]
    for i in cmds:
        if i == 'UP':
            size = []
            for j in range(matrixSize):
                size.append(j)
            if matrix.index(previous_point_value) not in size:
                location = matrix.index(previous_point_value)
                previous_point_value = matrix[location - matrixSize]
                print(previous_point_value)
        if i == 'DOWN':
            size = []
            length_matrix = len(matrix)
            for j in range(len(matrix) - matrixSize, length_matrix, 1):
                size.append(j)
            if matrix.index(previous_point_value) not in size:
                location = matrix.index(previous_point_value)
                previous_point_value = matrix[location + matrixSize]
                print(previous_point_value)
        if i == 'LEFT':
            size = []
            for j in range(0, len(matrix) - 1):
                if j % matrixSize == 0:
                    size.append(j)
            if matrix.index(previous_point_value) not in size:
                location = matrix.index(previous_point_value)
                previous_point_value = matrix[location - (matrixSize - (matrixSize - 1))]
                print(previous_point_value)
        if i == 'RIGHT':
            size = []
            j = -1
            while j <= len(matrix) and j + matrixSize <= len(matrix):
                j = j + matrixSize
                size.append(j)
            if matrix.index(previous_point_value) not in size:
                location = matrix.index(previous_point_value)
                previous_point_value = matrix[location + (matrixSize - (matrixSize - 1))]
                print(previous_point_value)
    return matrix[previous_point_value]
