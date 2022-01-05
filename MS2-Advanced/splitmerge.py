import cv2 as cv
import numpy as np

url = '../Resources/Photos/cats.jpg'
img = cv.imread(url)
cv.imshow('Cat', img)

## split to b,g,r color
b,g,r  = cv.split(img)

# cv.imshow('r', r)
# cv.imshow('g', g)
# cv.imshow('b', b)

## show the origin red, blue, and green color
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('red', red)
cv.imshow('green', green)
cv.imshow('blue', blue)

merged = cv.merge([b,g,r])
cv.imshow("merged", merged)

cv.waitKey(0)