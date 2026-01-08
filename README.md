# zdcf

This package wraps the classic **Z-transformed Discrete Correlation Function (ZDCF)** Fortran implementation using **NumPy f2py**.
See [Alexander (1997)](https://link.springer.com/chapter/10.1007/978-94-015-8941-3_14) for the original algorithm. 

## Install

You need a Fortran compiler (e.g., `gfortran`) installed. After cloning this repo, in the directory `zdcf` run the following:

```bash
python -m pip install -U pip
python -m pip install -U numpy meson-python
python -m pip install -U pytest
python -m pip install -e .
python -m pytest -vv
```

## Example usage

```python
import numpy as np
import zdcf

# Example input
ta = np.arange(1000, dtype=np.float32)
a = np.sin(ta)
erra = np.full_like(a, 0.01)

# Estimate ZDCF
lag, dcf = zdcf.compute(ta, a, erra, mbins=50, maxlag=50.0, res=0.0005)
```

See `examples/*` for more.

## Notes

This repository uses a `pyproject.toml` build with **Meson** via `meson-python`.
