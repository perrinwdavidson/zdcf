"""ZDCF: Z-transformed Discrete Correlation Function (Fortran + f2py)."""

from __future__ import annotations

from ._zdcf import zdcf  # raw f2py binding
from .api import compute

__all__ = ["zdcf", "compute"]
