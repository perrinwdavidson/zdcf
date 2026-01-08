import numpy as np
import zdcf

def test_import_and_call():
    t = np.linspace(0, 1, 10)
    x = np.sin(2*np.pi*t)
    err = 0.01*np.ones_like(t)

    # example signature: zdcf(t, x, err, mbins, maxlag, minbin, res)
    tau, dcf = zdcf._zdcf.zdcf(t, x, err, 2, 10.0, int(len(t)), 0.005, int(len(t)))
    assert tau.shape[0] == 2
    assert dcf.shape[0] == 2
