import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_a = np.array(y_true)
    y_b = np.array(y_pred)

    SS_res = np.sum(np.square(y_a - y_b))

    y_avg = np.mean(y_a)
    SS_tot = np.sum(np.square(y_a - y_avg))

    if SS_tot == 0:
        if SS_res == 0:
            return 1.0
        else:
            return 0.0

    R_2 = 1 - (SS_res / SS_tot)

    return R_2 
    
    pass