import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import resize
url = '../Resources/Photos/group 1.jpg'

img = cv.imread(url)

cv.imshow("People", img)

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100,100)
cv.imshow("Translated", translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow("Translated", rotated)   

# resized
resized = cv.resize(img, (500,500), cv.INTER_CUBIC)
cv.imshow("Resize", resized)

# flip
fliped = cv.flip(img, 1)
cv.imshow("Flip", fliped)

# chopped 
chopped = img[50:100,200:300]
cv.imshow("Chopped", chopped)

cv.waitKey(0)