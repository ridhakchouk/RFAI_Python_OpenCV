import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)

#cmap = palette de couleur
#interpolation = agit sur le contour des formes
plt.imshow(img, interpolation = 'bicubic')



plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


color = int(img[100, 100])
im_rgb = img[:, :, [2, 1, 0]]
# if image type is b g r, then b g r value will be displayed.
# if image is gray then color intensity will be displayed.
print(color)