import numpy as np
import matplotlib as mpl
from functions import multi_brot
from matplotlib.colors import LogNorm


def calc_fractal(size, x_min, x_max, y_min, y_max, max_iter, threshold, start, func):
    # linear space for both axis of the complex plane
    x = np.linspace(x_min, x_max, size)
    y = np.linspace(y_min, y_max, size)

    c = x + y[:, None] * 1j
    z_val = np.full(np.shape(c), start, dtype=np.complex64)

    # create a new array to put the number of iterations into and the values of z
    n_iter = np.zeros(np.shape(c), dtype=int)

    for n in range(max_iter):
        print(f'{n * 100 / (max_iter - 1):.1f}% done, iteration: {n}/{max_iter - 1}', end='\r')
        if start == 0:  # mandelbrot algorithm
            I = np.less(abs(z_val), threshold)
            n_iter[I] = n
            z_val[I] = func(z_val[I], c[I])
        else:  # julia algorithm
            I = np.less(abs(c), threshold)
            n_iter[I] = n
            c[I] = func(c[I], z_val[I])
    print(f'{"Done": ^40}', end='\r')

    # all values that didn't explode are 0
    n_iter[n_iter == max_iter - 1] = 0
    return n_iter


def plot_fractal(ax, x_min, x_max, y_min, y_max, size, max_iter, threshold, cmap_name, start=0, func=multi_brot):
    n_iter = calc_fractal(size, x_min, x_max, y_min, y_max, max_iter, threshold, start, func)
    cmap = mpl.cm.get_cmap('hsv')
    img = ax.imshow(n_iter, extent=[x_min, x_max, y_min, y_max], cmap=cmap, norm=LogNorm(vmin=3, vmax=48))
    ax.axis('scaled')
    ax.set_facecolor('black')
    ax.set_xlabel('Real axis')
    ax.set_ylabel('Imaginary axis')