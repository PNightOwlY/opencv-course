import cv2 as cv
import numpy as np

url = '../Resources/Photos/group 1.jpg'
img = cv.imread(url)
cv.imshow('Lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)


haar_cascade = cv.CascadeClassifier('/Users/mac/Desktop/HU_2020/ms-proj-h22-sum/opencv-course/MS3-Faces/haar_face.xml')

# the accuracy is influenced by scaleFactor, minNeighbors
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f'{len(faces_rect)} faces found!')

for (x,y,w,h) in faces_rect:
    rect = cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    
cv.imshow("Face detaction", img)
cv.waitKey(0)