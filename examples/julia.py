import matplotlib.pyplot as plt
from fractals import plot_fractal

julia_cst = {
    'x_min_l': [-1.5,-1.5, -1.5, -1.5],
    'x_max_l': [1.5, 1.5, 1.5, 1.5],
    'y_min_l': [-1.5,-1.5, -1.5, -1.5],
    'y_max_l': [1.5, 1.5, 1.5, 1.5],
    'cst': [-0.8j, -0.4 + 0.6j, 0.285 + 0.01j, -0.7269 + 0.1889j]
}


def julia(plot_cst):
    f, axes = plt.subplots(nrows=2, ncols=2, figsize=(8.5, 8.5), constrained_layout=True)
    f.suptitle("The julia set")
    for n, (ax, x_min, x_max, y_min, y_max, c) in enumerate(zip(axes.ravel(), *(julia_cst.values()))):
        plot_fractal(ax, x_min, x_max, y_min, y_max, **plot_cst, start=c)
        ax.set_title(f'$z^2 + {c}$')
    plt.savefig('figures\\Julia.png', dpi=500)
    plt.show()
