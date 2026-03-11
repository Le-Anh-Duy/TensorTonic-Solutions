import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here

    if max_len is None:
        max_len = max(len(x) for x in seqs)

    pad = [pad_value for x in range(max_len)]

    res = np.full((len(seqs), max_len), pad_value)
    i = 0

    for i, seq in enumerate(seqs):
        cur_len = min(len(seq), max_len)
        res[i][:cur_len] = np.array(seqs[i][:cur_len])
    return res