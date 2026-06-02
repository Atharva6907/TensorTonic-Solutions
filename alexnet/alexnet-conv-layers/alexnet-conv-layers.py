import numpy as np

def alexnet_conv1(image: np.ndarray) -> np.ndarray:
    """
    AlexNet first conv layer: 11x11, stride 4, 96 filters (shape simulation).
    """
    # YOUR CODE HERE
    batch_size = image.shape[0]
    in_height = image.shape[1]
    in_width = image.shape[2]

    k = 11     
    s = 4       
    p = 2     
    filters = 96 

    out_height = (in_height + 2 * p - k) // s + 1
    out_width = (in_width + 2 * p - k) // s + 1

    return np.zeros((batch_size, out_height, out_width, filters))
    pass