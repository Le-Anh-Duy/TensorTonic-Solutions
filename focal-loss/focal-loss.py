import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    pass

    P = np.array(p)
    Y = np.array(y)
    n = len(p)

    res = - (1 - P) ** gamma * Y * np.log(P) - P ** gamma * (1 - Y) * np.log(1 - P)
    return res.sum() / n
