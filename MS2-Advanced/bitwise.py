import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255,-1)

cv.imshow("circle", circle)
cv.imshow("rectangle", rectangle)

# 交集
bitwise_and = cv.bitwise_and(circle, rectangle)
# 并集
bitwise_or = cv.bitwise_or(circle, rectangle)
# 差集
bitwise_xor = cv.bitwise_xor(circle, rectangle)

circle_not = cv.bitwise_not(circle)
cv.imshow("Bitwise and",bitwise_and)
cv.imshow("Bitwise or", bitwise_or)
cv.imshow("bitwise_xor",bitwise_xor)
cv.imshow("Circle_not", circle_not)

cv.waitKey(0)