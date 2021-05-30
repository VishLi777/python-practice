import numpy as np
import matplotlib.pyplot as plt


def julia_set(c=-0.8 + 0.156j, height=600, width=900, x=0, y=0, zoom=1, max_iterations=150):
    x_width = 1.5
    x_from = x - x_width / zoom
    x_to = x + x_width / zoom

    x = np.linspace(x_from, x_to, width).reshape((1, width))

    y_height = 1.5 * height / width
    y_from = y - y_height / zoom
    y_to = y + y_height / zoom

    y = np.linspace(y_from, y_to, height).reshape((height, 1))

    z = x + 1j * y

    c = np.full(z.shape, c)

    div_time = np.zeros(z.shape, dtype=int)
    m = np.full(c.shape, True, dtype=bool)

    for i in range(max_iterations):
        z[m] = z[m] ** 2 + c[m]

        m[np.abs(z) > 2] = False

        div_time[m] = i
    return div_time


plt.imshow(julia_set(), cmap='magma')
plt.imshow(julia_set(c=-0.4 + 0.6j, max_iterations=100), cmap='magma')

plt.show()