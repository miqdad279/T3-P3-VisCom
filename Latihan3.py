from email.mime import image
import cv2 as cv
import numpy as np

image = cv.imread("template.png",0)
if image is None:
    exit(0)

try:
    bright = int(input('* Enter the brightness value [0-255]: '))
except ValueError:
    print('Error, not a number')

new_image = np.zeros(image.shape, image.dtype)

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
            newVal = image[y,x] - bright
            if newVal > 255:
                newVal = 255
            new_image[y,x] = newVal

cv.imshow('Original Image', image)
cv.imshow('Brightness Image', new_image)
cv.waitKey()