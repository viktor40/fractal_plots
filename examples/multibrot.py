import matplotlib.pyplot as plt
from fractals import plot_fractal
from functions import multi_brot
from functools import partial

multi_brot_cst = {
    'x_min_l': [-1.5, -1.4, -1, -1.25],
    'x_max_l': [1.5, 1.1, 1, 1.25],
    'y_min_l': [-1.5, -1.25, -1, -1.25],
    'y_max_l': [1.5, 1.25, 1, 1.25],
}


def multibrot(plot_cst):
    f, axes = plt.subplots(nrows=2, ncols=2, figsize=(8.5, 8.5), constrained_layout=True)
    f.suptitle("The multibrotset")
    for n, (ax, x_min, x_max, y_min, y_max) in enumerate(zip(axes.ravel(), *(multi_brot_cst.values()))):
        plot_fractal(ax, x_min, x_max, y_min, y_max, **plot_cst, func=partial(multi_brot, n=n+3))
        ax.set_title('$z^{' + f'{n+3}' + '} + c$')
    plt.savefig('figures\\Multibrot.png', dpi=500, )
    plt.show()
