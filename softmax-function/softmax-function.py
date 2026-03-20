import numpy as np

def softmax(arr):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here


    x = np.array(arr)
    x = x - x.max()
    x = np.exp(x)

    if x.ndim == 1:
        s = x.sum()
        x = x / s
    else:
        s = x.sum(axis=1)
        x = x / s[:, np.newaxis]

    return x
    