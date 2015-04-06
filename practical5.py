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

def multiply_matrix(matrix1=[[1, 2, 3], [1,0, 0]], matrix2=[[1,1,1], [1,1,1], [1,1,2]]):
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
