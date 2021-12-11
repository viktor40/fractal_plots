import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LogNorm
from functions import multi_brot
from fractals import calc_fractal

rcParams['animation.ffmpeg_path'] = 'C:\\Program Files\\FFmpeg\\bin\\ffmpeg.exe'

julia_anim_cst = {
    'size': 5000,
    'max_iter': 50,
    'threshold': 10,
    'x_min': -1.5,
    'x_max': 1.5,
    'y_min': -1.5,
    'y_max': 1.5,
}


def julia_animation():
    # init plots
    f, axes = plt.subplots(nrows=1, ncols=1, figsize=(5, 4.5))

    z = calc_fractal(**julia_anim_cst, start=1 + 0j, func=multi_brot)
    c_map = cm.get_cmap('hsv')
    cst_space = np.linspace(0, 2 * np.pi, 722)
    img = axes.imshow(z, extent=[-1.5, 1.5, -1.5, 1.5], cmap=c_map, norm=LogNorm(vmin=3, vmax=48))
    f.suptitle(r'Animation of the julia set for $z = 0.7885 \cdot e^{i \theta}$ with $\theta \in [0, 2\pi]$')
    axes.axis('scaled')
    axes.set_facecolor('black')
    axes.set_xlabel('Real axis')
    axes.set_ylabel('Imaginary axis')

    def animate(i):
        cst = 0.7885 * np.exp(1j * cst_space[i + 1])
        new_z = calc_fractal(**julia_anim_cst, start=cst, func=multi_brot)
        img.set_data(new_z)
        return f,

    # start an animation
    anim = FuncAnimation(f, animate, interval=20, frames=720, blit=True, repeat=False)

    try:
        anim.save("animations\\Animation_julia_set.mp4", writer='ffmpeg', fps=30, dpi=500)
    except Exception as e:
        print(e)
        print('Saving of the animation failed.')

    plt.close(f)
