import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    a = np.array(X)
    b = np.array(y)
    
    a_t = np.transpose(a)
    b_t = np.transpose(b)
    
    first = np.matmul(a_t, a)
    second = np.matmul(a_t, b)
    
    first_inverse = np.linalg.inv(first)
    w = np.matmul(first_inverse, second)

    return w
    pass