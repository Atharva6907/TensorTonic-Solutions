import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_t = np.array(y_true)
    y_p = np.array(y_pred)
    
    squared_errors = np.square(y_p - y_t)

    mse = np.mean(squared_errors)
    
    return mse
    
    pass
