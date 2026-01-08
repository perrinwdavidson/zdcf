# =========================================================
# run_zdcf.py
# ---------------------------------------------------------
# run the following in environment of your choice ::
# > python -m pip install -U pip
# > python -m pip install -U numpy meson-python
# > python -m pip install -U pytest
# > python -m pip install -e .
# > python -m pytest -vv
# N.B.: You MUST have a Fortran compiler available (gfortran/ifort/ifx/etc.)
# ---------------------------------------------------------
# configure -----------------------------------------------
# import ::
import zdcf
import numpy as np
import matplotlib.pyplot as plt

# set plotting ::
fontsize = 7
linewidth = 0.5
ticklength = 2.5
plt.rc("text", usetex=True)
plt.rcParams.update({"font.size": fontsize})
plt.rc("font", family="Helvetica")
plt.rc("text.latex", preamble=r"""
       \usepackage{wasysym}
       \renewcommand{\rmdefault}{phv}
       \renewcommand{\sfdefault}{phv}
       \usepackage{sansmath}
       \sansmath""")

# functions -----------------------------------------------
def run(data: np.ndarray(), nlags: int, maxlag: float, res: float) -> np.ndarray():
    t, x, err = data[:, 0], data[:, 1], data[:, 2]
    tau, R0 = zdcf.compute(t, x, err, mbins=nlags, maxlag=maxlag, res=res)
    R = np.array((tau, R0)).T
    R = R[tau!=0, :]
    return R

def main():
    # load data ::
    data = np.loadtxt("examples/data/data_raw/d13c.txt", delimiter="\t")

    # run zdcf ::
    nlags = 1000
    maxlag = 9000000
    res = 0.0005
    R = run(data, nlags, maxlag, res)

    # plot output ::
    dx = 8.7 / 2.54
    dy = dx
    fig, ax = plt.subplots(1, 1, figsize=(dx, dy), constrained_layout=True)
    ax.scatter(R[:, 0] / 1000, R[:, 1], c="k")
    ax.set_yscale("log")
    ax.set_xlabel(r"Lags, $\tau$ $($kyr$)$")
    ax.set_ylabel(r"Autocorrelation, $R(\tau)$")
    plt.savefig("examples/plots/cenozoic_autocorrelation.pdf")
    plt.show()
    plt.close()

    # save output ::
    np.savetxt("examples/data/sim/cenozoic_autocorrelation.txt", R, delimiter="\t")

# run analysis --------------------------------------------
if __name__ == "__main__":
    main()

# =========================================================
