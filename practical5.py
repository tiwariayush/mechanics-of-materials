#!/usr/bin/python

import math
import numpy

def enter_matrix():
    """
        Function to get a matrix using raw_input of m no. of
        rows and n no. of columns
    """

    m = int(raw_input("Enter n, i.e, number of rows:"))
    n = int(raw_input("Enter m, i.e, number of columns:"))

    matrix = []
    for i in xrange(m):
        row = []
        for j in xrange(n):
            row.append(float(raw_input()))
        matrix.append(row)

    return matrix

def multiply_matrix(matrix1, matrix2):
    """
        Function to multiply two matrix with each other and
        return a final matrix. This takes two matrix as argument.
        The datatype of the matrix would be a 2-D list/array.
    """

    if not len(matrix1[0])==len(matrix2):
        return "Matrices are not multiplicable"


    multiplication_matrix = []
    for k in xrange(len(matrix1)):
        row = []
        for i in xrange(len(matrix2)):
            point = 0
            for j in xrange(len(matrix1[k])):
                point = point + matrix1[k][j]*matrix2[j][i]
            row.append(point)
        multiplication_matrix.append(row)

    return multiplication_matrix


# Now we will use the numpy library to work with diffrent functions on matrix.
# This can be achieved by using numpy.array function which will convert a 2-D
# array into a numpy array on which inbuilt functions can be applied.

def multiply_matrix_numpy(matrix1, matrix2):
    """
        This function will multiply 2 matrices and give a numpy 
        array using numpy dot function
    """

    return numpy.dot(matrix1, matrix2)

def compare_multilied_matrices(matrix1, matrix2):

    multiplied_matrix_manual =numpy.array(multiply_matrix(matrix1, matrix2))
    multiplied_matrix_numpy = multiply_matrix_numpy(matrix1, matrix2)

    return multiplied_matrix_manual==multiplied_matrix_numpy

def coordinate_tranformation(angle, matrix):
    """
        Function to transform a given matrix to another one 
        when the coordinate axis is rotated by angle given.
        The angle is angle between original and transformed
        X-axis in anti-clockwise direction.
    """

    transformation_matrix = [[math.cos(angle), math.cos(math.pi/2-angle), math.cos(pi/2)],
                             [math.cos(math.pi/2+angle), math.cos(angle), math.cos(pi/2)],
                             [math.cos(pi/2), math.cos(pi/2), math.cos(0)]]

    
    m1 = multiply_matrix_numpy(transformation_matrix, matrix)

    return multiply_matrix_numpy(numpy.array(m1), numpy.array(transformation_matrix.T))
