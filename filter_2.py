import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
imgo = cv.imread('grupo.jpeg')
img = cv.cvtColor(imgo, cv.COLOR_BGR2RGB)
assert img is not None, "file could not be read, check with os.path.exists()"
median = cv.bilateralFilter(img,9,75,75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
