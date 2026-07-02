import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Convert input to a NumPy array in case it's passed as a list
    x = np.asarray(x)
    
    if p < 0 or p > 1:
        raise ValueError("Dropout probability p must be in the range [0, 1].")
        
    if rng is None:
        rng = np.random.default_rng()
        
    keep_p = 1.0 - p
    
    if keep_p == 0.0:
        return np.zeros_like(x), np.zeros_like(x)
        
    random_values = rng.random(x.shape)
    
    
    dropout_pattern = np.where(random_values < keep_p, 1.0 / keep_p, 0.0)
    
    output = x * dropout_pattern
    
    return output, dropout_pattern