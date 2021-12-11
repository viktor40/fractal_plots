import matplotlib.pyplot as plt
from fractals import plot_fractal
from functions import multi_brot
from functools import partial

multi_julia_cst = {
    'x_min_l': [-1.7,-1.5, -1.5, -1.5],
    'x_max_l': [1.7, 1.5, 1.5, 1.5],
    'y_min_l': [-1.7,-1.5, -1.5, -1.5],
    'y_max_l': [1.7, 1.5, 1.5, 1.5],
    'cst': [-0.70176 - 0.3842j, 0.4 + 0.002275j, 0.559 - 0.0481j, 0.736 - 0.417355j]
}


def multi_julia(plot_cst):
    f, axes = plt.subplots(nrows=2, ncols=2, figsize=(8.5, 8.5), constrained_layout=True)
    f.suptitle("The multi julia set")
    powers = [2, 3, 4, 6]
    for ax, x_min, x_max, y_min, y_max, c, p in zip(axes.ravel(), *(multi_julia_cst.values()), powers):
        plot_fractal(ax, x_min, x_max, y_min, y_max, **plot_cst, start=c, func=partial(multi_brot, n=p))
        ax.set_title(f'$z^{p} + {c}$')
    plt.savefig('figures\\Multi_Julia.png', dpi=500, )
    plt.show()
