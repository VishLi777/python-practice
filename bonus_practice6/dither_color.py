import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


def dither(image):
    res = np.copy(image)

    for y in range(1, image.shape[0] - 1):
        for x in range(1, image.shape[1] - 1):
            pixel = res[y][x]

            pixel_color = round(pixel / 255) * 255
            res[y][x] = pixel_color
            error = pixel - pixel_color

            res[y][x + 1] += 7 / 16 * error
            res[y + 1][x + 1] += 1 / 16 * error
            res[y + 1][x] += 5 / 16 * error
            res[y + 1][x - 1] += 3 / 16 * error

    return res


img = np.array(cv.cvtColor(cv.imread("dither.jpeg"), cv.COLOR_BGR2GRAY), dtype=int)

plt.imshow(dither(img), cmap="gray")
plt.show()
