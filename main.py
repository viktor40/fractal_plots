from examples.mandelbrot import mandelbrot
from examples.multibrot import multibrot
from examples.julia import julia
from examples.multi_julia import multi_julia
from examples.mandelbrot_like import mandelbrot_like
from examples.julia_animation import julia_animation

plot_cst = {
    'size': 1000,
    'max_iter': 50,
    'threshold': 50,
    'cmap_name': 'hsv'
}


def main():
    julia_animation()


if __name__ == '__main__':
    main()
