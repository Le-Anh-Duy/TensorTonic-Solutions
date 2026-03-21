def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here

    v = sorted(values)

    n = len(values)
    if n == 1:
        return [0.0]
    
    med = (v[n // 2] + v[(n - 1) // 2]) / 2

    n2 = n // 2

    med_left = (v[n2 // 2] + v[(n2 - 1) // 2]) / 2
    buffer = n2 + n % 2
    med_right = (v[buffer + n2 // 2] + v[buffer + (n2 - 1) // 2]) / 2
    f = (med_right - med_left)
    if f >= 0 and f < 1e-8:
        f = 1
    res = [float((x - med) / f) for x in values]
    return res