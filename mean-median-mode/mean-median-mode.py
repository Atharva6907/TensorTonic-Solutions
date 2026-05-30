import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    data = np.array(x)
    counts = Counter(data)
    max_count = max(counts.values())

    all_modes = [value for value, count in counts.items() if count == max_count]
    mode_val = min(all_modes)

    mean_val = np.mean(data)
    median_val = np.median(data)
    
    return (float(mean_val), float(median_val), float(mode_val))
    pass