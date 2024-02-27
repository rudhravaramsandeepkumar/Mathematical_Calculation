import numpy as np
import mpmath as mp


def get_matrix(temp_matrix_a):
    matrix_ = []
    for string in temp_matrix_a:
        nums = []
        for num in string.split(','):
            if num.isdigit():
                nums.append(int(num))
            else:
                nums.append(num)  # append the string as is
        matrix_.append(nums)
    return matrix_


def is_valid(matrix):
    for row in matrix:
        for element in row:
            if not isinstance(element, int):
                return False
    return True


def matrix_arithmetic(A, B):
    check_valid_a = A
    check_valid_B = B
    try:
        A = np.array(A)
    except ValueError:
        return {'OutPut': 'Please check matrice 1'}
    try:
        B = np.array(B)
    except ValueError:
        return {'OutPut': 'Please check matrice 2'}
    if A.shape != B.shape:
        return {'OutPut': 'The input matrices have different shapes'}
    if not is_valid(check_valid_a):
        return {'OutPut': 'Please check matrix 1'}
    if not is_valid(check_valid_B):
        return {'OutPut': 'Please check matrix 2'}
    return {'OutPut': 'Successful'}


def matrix_arithmetic_operations(A, B, operation):
    A = np.array(A)
    B = np.array(B)
    if operation == '+':
        C = np.add(A, B)
    elif operation == '-':
        C = np.subtract(A, B)
    elif operation == '*':
        C = np.multiply(A, B)
    elif operation == '/':
        C = np.divide(A, B)
    else:
        return None
    return C


def get_ones_zeros_eye(matrix, type):
    if type == 'Zeros':
        matrix = np.zeros(matrix)
    elif type == 'Ones':
        matrix = np.ones(matrix)
    elif type == 'Eyes':
        matrix = np.eye(matrix)
    return matrix


def get_transpose_inv_det(matrix, type):
    mp.dps = 5
    check_valid_a = matrix
    try:
        matrix = np.array(matrix)
        matrix_final = np.array(matrix)
    except ValueError:
        return 'Please check matrix expression'
    if not is_valid(check_valid_a):
        return 'Please check matrix expression'
    if matrix.shape[0] == matrix.shape[1]:
        det = np.linalg.det(matrix)
        if det != 0:
            matrix_mpf = mp.matrix(matrix.tolist())
            det = mp.det(matrix_mpf)
            transpose_matrix = np.transpose(matrix)
            inv_matrix = np.linalg.inv(matrix_final)
            if type=='Det':
                return det
            elif type=='Transpose':
                return transpose_matrix
            else:
                return inv_matrix
        else:
            return "The matrix is singular"
    else:
        return "The matrix is not square"


def get_Diagonal_Trace_Size(matrix, type):
    check_valid_a = matrix
    try:
        matrix = np.array(matrix)
    except ValueError:
        return 'Please check matrix expression'
    if not is_valid(check_valid_a):
        return 'Please check matrix expression'
    if type=='Diagonal':
        diagonal = np.diag(matrix)
        return diagonal
    elif type == 'Size':
        size = matrix.shape
        return size
    else:
        trace = np.trace(matrix)
        return trace


