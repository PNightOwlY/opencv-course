import cv2 as cv
import numpy as np
from numpy.lib.histograms import histogram

url = '../Resources/Photos/park.jpg'
img = cv.imread(url)
cv.imshow('travel', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.abs(lap))
cv.imshow("Laplacian", lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow("Sobelx", sobelx)
cv.imshow("SobelY", sobely)

sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow("Sobel", sobel)

# candy
canny = cv.Canny(gray, 150, 175)
cv.imshow("candy", canny)

cv.waitKey(0)