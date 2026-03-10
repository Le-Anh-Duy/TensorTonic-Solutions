import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """

    b = np.arange(0, d_model) // 2
    b = np.exp(b * (-2 / d_model * np.log(base)))
    pos = np.arange(0, seq_len)
    
    v = np.outer(pos, b)

    v[::,0:d_model:2] = np.sin(v[::,0:d_model:2])
    v[::,1:d_model:2] = np.cos(v[::,1:d_model:2])

    return v