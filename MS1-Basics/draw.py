import cv2 as cv

import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

# cv.imshow('Blank', blank)

# blank[200:300, 300:400] = 0,255,0

# cv.imshow('Green Blank', blank)

# 画长方形
cv.rectangle(blank, (0,0), (100,100), color=(0,220,0), thickness=-1)
cv.imshow('Rectangle', blank)

# 画圆
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow("Circle", blank)

# 画线
cv.line(blank,(0,0),  (blank.shape[1]//2, blank.shape[0]//2), color=(0,255,0),thickness=3)
cv.imshow('Line', blank)

# 加文字
cv.putText(blank, "Hello world", (0,255), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,255),2)
cv.imshow('TEXT', blank)

cv.waitKey(0)
