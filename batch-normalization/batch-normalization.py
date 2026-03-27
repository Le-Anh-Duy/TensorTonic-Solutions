import numpy as np

def batch_norm_forward(input, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    # pass

    x = np.array(input)
    x_hat = np.zeros(x.shape)
    if len(x.shape) == 2:
        for i in range(x.shape[1]):
            u = np.mean(x[:,i])
            s2 = np.var(x[:,i])
            x_hat[:,i] = gamma[i] * (x[:,i] - u) / np.sqrt(s2 + eps) + beta[i]
    else:
        for i in range(x.shape[1]):
            u = np.mean(x[:,i,:,:])
            s2 = np.var(x[:,i,:,:])
            x_hat[:,i] = gamma[i] * (x[:,i,:,:] - u) / np.sqrt(s2 + eps) + beta[i]
            
    return x_hat