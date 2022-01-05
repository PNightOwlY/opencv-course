import cv2 as cv
import numpy as np

url = '../Resources/Photos/group 1.jpg'
# img = cv.imread(url)
# cv.imshow('Lady', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)

capture = cv.VideoCapture('/Users/mac/Desktop/PNight/u盘/纪念视频/AF51CA083048C120CB224BF14E5862CA.mp4')
haar_cascade = cv.CascadeClassifier('/Users/mac/Desktop/HU_2020/ms-proj-h22-sum/opencv-course/MS3-Faces/haar_face.xml')

while True:
    isTrue, img = capture.read()
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # the accuracy is influenced by scaleFactor, minNeighbors
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    print(f'{len(faces_rect)} faces found!')

    for (x,y,w,h) in faces_rect:
        rect = cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=1)
    cv.imshow("Face detaction", img)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cv.waitKey(0)