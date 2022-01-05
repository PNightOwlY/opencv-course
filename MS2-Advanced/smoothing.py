import cv2 as cv
import numpy as np

url = '../Resources/Photos/cats.jpg'
img = cv.imread(url)
cv.imshow('Cat', img)


# average blur
average = cv.blur(img, (3,3))
cv.imshow("Average", average)

# gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gauss', gauss)

# median 
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)