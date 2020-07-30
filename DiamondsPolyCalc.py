import regex as regex
from sympy import *
import fractions
import re

measure = {
    1: [1,3],
    2: [1,5,13],
    3: [1,7,25,63],
    4: [1,9,41,129,321],
    5: [1,11,61,231,681,1683],
    6: [1,13,85,377,1289,3653,8989],
    7: [1,15,113,575,2241,7183,19825,48639],
    8: [1,17,145,833,3649,13073,40081,108545,265729],
    9: [1,19,181,1159,5641,22363,75517,224143,598417,1462563],
    10: [1,21,221,1561,8361,36365,134245,433905,1256465,3317445,8097453],
    11: [1,23,265,2047,11969,56695,227305,795455,2485825,7059735,18474633,45046719]
}

def bernoulliTriangleBuilder(dimension):

    # Declare output list
    outputList = []

    # For I less than the dimension size
    for i in range(dimension):

        # Define a temporary holding list
        tempList = []

        # For j less than the size I
        for j in range(i+1):

            # If j is the first or last element in the array.
            if j == i or j == 0:

                # Append a 1 to the list
                tempList.append(1)

            # Otherwise Calculate the value
            else:

                # The value is always the previous entry in the outputlist of j + j-1
                tempList.append(outputList[i-1][j] + outputList[i-1][j-1])

        # Append the row to the list.
        outputList.append(tempList)

    return outputList

def buildMatrix(dimension):

    # Define matrix list
    matrix = []

    # For "dimension" amount of times
    for i in range(dimension + 1):

        # Define temp List
        tempList = []

        # For "dimension" amount of times
        for j in range(dimension + 1):

            # Add the powers to the list
            tempList.append(pow(i + 1, dimension - j))

        # Add the last item to the list
        tempList.append(measure[dimension][i])

        # Add the list to the matrix
        matrix.append(tempList)

    return Matrix(matrix)

def main():

    dim = 11

    matrix = Matrix(buildMatrix(dim))

    matrix = matrix.rref()

    print(str(matrix[0].col(-1)))

    q = matrix[0].col(-1)

    q = re.sub('([A-z()])', '', str(q)).split()

    print(q)

    lines = bernoulliTriangleBuilder(dim)

    print(str(lines))



if __name__ == "__main__":
    main()