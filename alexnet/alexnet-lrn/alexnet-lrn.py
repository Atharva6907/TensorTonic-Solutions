import numpy as np

def local_response_normalization(x: np.ndarray, k: float = 2, n: int = 5,
                                 alpha: float = 1e-4, beta: float = 0.75) -> np.ndarray:
    """
    Apply Local Response Normalization across channels.
    """
    C = x.shape[-1]
    
    squared = x ** 2
    
    output = np.zeros_like(x, dtype=float)
    
    for i in range(C):
        start_idx = max(0, i - n // 2)
        end_idx = min(C, i + n // 2 + 1)
        
        sum_sq_neighbors = np.sum(squared[..., start_idx:end_idx], axis=-1)
        
        output[..., i] = x[..., i] / ((k + alpha * sum_sq_neighbors) ** beta)
        
    return output