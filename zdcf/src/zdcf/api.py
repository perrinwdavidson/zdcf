from __future__ import annotations

import numpy as np

from ._zdcf import zdcf as _zdcf


def compute(ta, a, erra, mbins: int, maxlag: float, res: float):
    """Compute the ZDCF.

    Returns
    -------
    tau, dcf : ndarray
        1D arrays of length `mbins`.
    """
    ta = np.ascontiguousarray(ta, dtype=np.float32)
    a = np.ascontiguousarray(a, dtype=np.float32)
    erra = np.ascontiguousarray(erra, dtype=np.float32)

    if not (ta.ndim == a.ndim == erra.ndim == 1):
        raise ValueError('ta, a, erra must be 1D arrays')
    if not (len(ta) == len(a) == len(erra)):
        raise ValueError('ta, a, erra must have the same length')

    mpnts = int(len(ta))
    minbin = mpnts

    tau, dcf = _zdcf(ta, a, erra, int(mbins), float(maxlag), int(minbin), float(res), int(mpnts))
    return np.asarray(tau), np.asarray(dcf)
