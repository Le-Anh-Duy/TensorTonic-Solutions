import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    # pass

    g = np.array(grad, dtype = np.float64)
    theta = np.array(param,dtype = np.float64)
    
    m_new = beta1 * np.array(m, dtype=np.float64) + (1 - beta1) * g
    v_new = beta2 * np.array(v, dtype = np.float64)  + (1 - beta2) * g * g
    
    mt = m_new / (1 - beta1 ** t)
    vt = v_new / (1 - beta2 ** t)

    param_new = theta - lr * mt / (np.sqrt(vt) + eps)

    return (param_new, m_new, v_new)