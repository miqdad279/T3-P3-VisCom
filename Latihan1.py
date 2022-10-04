import cv2 as cv
import numpy as np

image = cv.imread("template.png", 1)
if image is None:
    print('Could not open or find the image: ')
    exit(0)

new_image = np.zeros(image.shape, image.dtype)
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for z in range(image.shape[2]):
            new_image[y, x, z] = 255 - image[y, x, z]

cv.imshow('Original Image', image)
cv.imshow('Negative Image', new_image)
cv.waitKey()