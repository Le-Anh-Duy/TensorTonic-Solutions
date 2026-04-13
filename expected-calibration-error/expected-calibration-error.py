import math
def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    bins = [0 for i in range(n_bins)]
    n = len(y_true)
    for y, p in zip(y_true, y_pred):
        idx = math.floor(p * n_bins)
        idx -= idx == n_bins
        bins[idx] += 1.0 * (y - p) / n

    ans = sum([abs(bins[idx]) for idx in range(n_bins)])
    

    return ans