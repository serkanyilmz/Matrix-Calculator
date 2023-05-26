from itertools import permutations
import copy
from fractions import Fraction

def transpose(matrix):
    transpose_matrix = []
    for j in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[j])
        transpose_matrix.append(new_row)
    return transpose_matrix

def determinant(matrix):
    def is_odd(perm):
        inversion = 0
        for x in range(len(perm)):
            for y in perm[x + 1:]:
                if perm[x] > y:
                    inversion += 1
        return inversion % 2
    if len(matrix) != len(matrix[0]):
        return "not_square_error"
    all_permutataions_of_j = list(permutations([x for x in range(len(matrix))]))
    total = 0
    for perm in all_permutataions_of_j:
        multiplication = 1
        for row_no in range(len(matrix)):
            multiplication *= matrix[row_no][perm[row_no]]
        total += multiplication * (-1) ** is_odd(perm)  # if is_even +=multiplication else -=multiplication
    return total

def matrix_addition(first_matrix, second_matrix):
    if len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0]):
        return "size_error"
    sum_matrix = []
    for x in range(len(first_matrix)):
        new_row=[]
        for y in range(len(first_matrix[0])):
            new_row.append(first_matrix[x][y] + second_matrix[x][y])
        sum_matrix.append(new_row)
    return sum_matrix


def matrix_subtraction(first_matrix, second_matrix):
    if len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0]):
        return "size_error"
    result_matrix = []
    for x in range(len(first_matrix)):
        new_row=[]
        for y in range(len(first_matrix[0])):
            new_row.append(first_matrix[x][y] - second_matrix[x][y])
        result_matrix.append(new_row)
    return result_matrix


def matrix_multiplication(first_matrix, second_matrix):
    if len(first_matrix[0]) != len(second_matrix):
        return "row_column_error"
    multiplication_matrix = []
    for x in range(len(first_matrix)):
        row = []
        for y in range(len(second_matrix[0])):
            total = 0
            for t in range(len(first_matrix[0])):
                total += first_matrix[x][t] * second_matrix[t][y]
            row.append(total)
        multiplication_matrix.append(row)
    return multiplication_matrix

def cramer(first_matrix, second_matrix):
    det_matr=determinant(first_matrix)
    if det_matr=="not_square_error":
        return "not_square_error"
    if len(second_matrix)!=len(first_matrix) or len(second_matrix[0])!=1:
        return "size_error"
    if det_matr==0:
        return "determinant_zero"
    xs=[]
    for c in range(len((first_matrix[0]))):
        replaced_matrix=copy.deepcopy(first_matrix)
        for r in range(len(first_matrix)):
            replaced_matrix[r][c]=second_matrix[r][0]
        x=Fraction(determinant(replaced_matrix))/det_matr
        xs.append([x])
    return xs


def inverse(matrix):
    det_matr=determinant(matrix)
    if det_matr=="not_square_error":
        return "not_square_error"
    if det_matr==0:
        return "determinant_zero"
    inv_matr=copy.deepcopy(matrix)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            mm=copy.deepcopy(matrix)
            mm.pop(r)
            for x in mm:
                x.pop(c)
            inv_matr[r][c]= ((-1)**(r+c))*determinant(mm)
    inv_matr=transpose(inv_matr)
    inv_matr=multiply_by(inv_matr,Fraction(1,det_matr))
    return(inv_matr)

def trace(matrix):
    if len(matrix) != len(matrix[0]):
        return "not_square_error"
    trace_of_matrix=0
    for x in range(len(matrix)):
        trace_of_matrix+=matrix[x][x]
    return trace_of_matrix

def multiply_by(matrix,num):
    mult_matr=copy.deepcopy(matrix)
    for r in range(len(mult_matr)):
        for c in range(len(mult_matr[r])):
            mult_matr[r][c]*=num
    return mult_matr

def add_up_with(matrix,num):
    result_matrix=copy.deepcopy(matrix)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            result_matrix[r][c]+=num
    return result_matrix