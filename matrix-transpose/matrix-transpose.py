import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    B = np.array(A)
    a, b = B.shape
    new_mat = np.zeros((b, a), dtype= B.dtype)
    for i in range(a):
        for j in range(b):
            new_mat[j, i] = B[i, j]

    return new_mat
    pass
