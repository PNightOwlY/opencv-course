
import cv2 as cv
import numpy as np
from numpy.lib.histograms import histogram

url = '../Resources/Photos/cats.jpg'
img = cv.imread(url)
cv.imshow('travel', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# simple threshold 
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple threshold", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple threshold inverse", thresh_inv)


# Adapt threshold 
adaptiveThreshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow("Adaptive threshold", adaptiveThreshold)

cv.waitKey(0)