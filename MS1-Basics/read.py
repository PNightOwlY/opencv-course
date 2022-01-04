import cv2 as cv

# 读取图片，写入图片路径
url = '../Resources/Photos/cat.jpg'

img = cv.imread(url)

cv.imshow('Cat', img)

cv.waitKey(0)

# 读取视频
url = '../Resources/Videos/dog.mp4'

capture = cv.VideoCapture(url)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# cv.waitKey(0)

# 215 error : cannot find the frame anymore