
import cv2 as cv
import numpy as np
from numpy.lib.histograms import histogram

url = '../Resources/Photos/cats.jpg'
img = cv.imread(url)
cv.imshow('travel', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


blank = np.zeros(img.shape[:2],dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2),
100, 255, -1)

masked = cv.bitwise_and(mask, gray)
cv.imshow("masked", masked)

hist = cv.calcHist([gray], [0], mask, [256], [0,256])
import matplotlib.pyplot as plt

# plt.figure()
# plt.title("Histogram of pixes")
# plt.xlabel("color of pixes")
# plt.plot(hist)
# plt.xlim((0,256))
# plt.show()
# cv.waitKey(0)   

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked", masked)

plt.figure()
plt.title("Histogram of pixes")
plt.xlabel("color of pixes")
plt.xlim((0,256))
colour = ('b','g','r')
for i, col in enumerate(colour):
    hist = cv.calcHist([img],[i], mask, [256], [0,256])
    plt.plot(hist)

plt.show()
