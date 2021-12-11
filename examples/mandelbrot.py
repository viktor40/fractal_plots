import matplotlib.pyplot as plt
from fractals import plot_fractal

brot_cst = {
    'x_min_l': [-2, -1.235, -1.9, -0.34],
    'x_max_l': [1, -1.275, -1.65, -0.26],
    'y_min_l': [-1.5, 0.36, -0.125, -0.685],
    'y_max_l': [1.5, 0.4, 0.125, -0.605],
}


def mandelbrot(plot_cst):
    f, axes = plt.subplots(nrows=2, ncols=2, figsize=(8.5, 8.5), constrained_layout=True)
    f.suptitle("The Mandelbrotset")
    for ax, x_min, x_max, y_min, y_max in zip(axes.ravel(), *(brot_cst.values())):
        plot_fractal(ax, x_min, x_max, y_min, y_max, **plot_cst)
    plt.savefig('figures\\Mandelbrot.png', dpi=500)
    plt.show()
