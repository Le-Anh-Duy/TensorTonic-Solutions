import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here

    if max_len is None:
        max_len = max([len(x) for x in seqs])

    pad = [pad_value for x in range(max_len)]

    res = seqs.copy()
    i = 0
    for seq in res:

        if len(seq) <= max_len:
            res[i] = seq + pad[0:max_len - len(seq)]
        else:
            res[i] = seq[0:max_len]
        i += 1
        # print(res)

    # print(max_len)
    return res