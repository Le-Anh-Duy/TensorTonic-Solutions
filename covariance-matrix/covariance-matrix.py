import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    x = np.array(X)

    s = x.shape
    if len(s) < 2 or s[0] < 2:
        return None
    
    m = np.mean(x, axis = 0)
    x_center = x - m
    n = s[0]
    sigma = x_center.T @ x_center 
    return 1.0 / (n - 1) * sigma