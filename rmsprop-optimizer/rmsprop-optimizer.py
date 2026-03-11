import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    gt = np.array(g, dtype=np.float64)
    st = beta * np.array(s, dtype=np.float64) + (1 - beta) * gt ** 2
    wt = w - lr * gt / np.sqrt(st + eps)
    return (wt, st)