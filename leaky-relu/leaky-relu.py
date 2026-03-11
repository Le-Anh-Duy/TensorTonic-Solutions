import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    res = np.array(x, dtype=np.float32)
    res[res < 0] = res[res < 0] * alpha
    return res