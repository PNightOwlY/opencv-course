import cv2 as cv
import numpy as np

url = '../Resources/Photos/cats.jpg'
img = cv.imread(url)
cv.imshow('Cat', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BGR HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)

# BGR to RGB
RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', RGB)

# matplotlib
import matplotlib.pyplot as plt
plt.imshow(RGB)
plt.show()
cv.waitKey(0)