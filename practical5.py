#!/usr/bin/python

import math
import numpy

def enter_matrix():
    """
        Function to get a matrix using raw_input of n no. of
        rows and m no. of columns
    """

    n = int(raw_input("Enter n, i.e, number of rows:"))
    m = int(raw_input("Enter m, i.e, number of columns:"))

    matrix = []
    for i in xrange(n):
        row = []
        for j in xrange(m):
            row.append(float(raw_input()))
        matrix.append(row)

    return matrix

def multiply_matrix(matrix1, matrix2):
    """
        Function to multiply two matrix with each other and
        return a final matrix. This takes two matrix as argument.
        The datatype of the matrix would be a 2-D list/array.
    """

    for i in matrix1:
        for j in i:
            pass
