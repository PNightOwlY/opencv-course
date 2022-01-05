import os
import cv2 as cv
import numpy as np

people = os.listdir('/Users/mac/Desktop/HU_2020/ms-proj-h22-sum/opencv-course/Resources/Faces/train')
dir = "/Users/mac/Desktop/HU_2020/ms-proj-h22-sum/opencv-course/Resources/Faces/train"
haar_cascade = cv.CascadeClassifier('/Users/mac/Desktop/HU_2020/ms-proj-h22-sum/opencv-course/MS3-Faces/haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(dir, person)
        label = people.index(person)

        for img in os.listdir(path=path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

            for (x,y,w,h) in faces_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()

features, labels = np.array(features, dtype="object"), np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')

print('Train done!')
