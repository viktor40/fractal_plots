import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from fractals import plot_fractal
from functions import cos, exp, cosh, poly2


variations_cst = {
    'x_min_l': [-3*np.pi, -1.5, -4, -3],
    'x_max_l': [3*np.pi, 4.5, 4, 1],
    'y_min_l': [-np.pi, -3, -9, -2],
    'y_max_l': [np.pi, 3, 9, 2],
    'titles': [r'$\cos(z) + c$', r'$e^z + c$', r'$\cosh(z) + c$', r'$z^2 + z + c$']
}


def mandelbrot_like(plot_cst):
    # init figure
    f = plt.figure(figsize=(9, 12), constrained_layout=True)

    # use GridSpec to divide the figure into subplots
    gs = GridSpec(3, 2, figure=f)
    plots = [
        f.add_subplot(gs[0, :]),
        f.add_subplot(gs[1, :-1]),
        f.add_subplot(gs[1:, -1]),
        f.add_subplot(gs[-1, 0])
    ]

    f.suptitle("Different mandelbrot like fractals")
    funcs = [cos, exp, cosh, poly2]
    for ax, func, x_min, x_max, y_min, y_max, title in zip(plots, funcs, *(variations_cst.values())):
        plot_fractal(ax, x_min, x_max, y_min, y_max, **plot_cst, func=func)
        ax.set_title(title)
    plt.savefig('figures\\Mandelbrot_like.png', dpi=500)
    plt.show()

