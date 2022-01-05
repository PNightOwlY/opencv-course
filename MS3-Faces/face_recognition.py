import cv2 as cv
import numpy as np
import os

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('/Users/mac/Desktop/HU_2020/ms-proj-h22-sum/opencv-course/MS3-Faces/face_trained.yml')

haar_cascade = cv.CascadeClassifier('/Users/mac/Desktop/HU_2020/ms-proj-h22-sum/opencv-course/MS3-Faces/haar_face.xml')

dir = '/Users/mac/Desktop/HU_2020/ms-proj-h22-sum/opencv-course/Resources/Faces/val'
people = os.listdir(dir)

features = []
labels = []
correct = 0
total = 0
for person in people:
    path = os.path.join(dir, person)

    for img in os.listdir(path):
        img_path = os.path.join(path, img)
        
        img_data = cv.imread(img_path)

        gray = cv.cvtColor(img_data, cv.COLOR_BGR2GRAY)

        face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        total += len(face_rect)

        for (x,y,w,h) in face_rect:
            face = gray[y:y+h, x:x+w]

            label, confidence = face_recognizer.predict(face)

            print(f'True name is {person}, and predict is {people[label]}, confidence {confidence}')

            correct += person==people[label]

            cv.putText(img_data, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=1)

            cv.rectangle(img_data, (x,y),(x+w,y+h), (0,255,0),thickness=2)

        cv.imshow(f"Detected Face {img_path}", img_data)


print(f"Accuracy is {correct/total}, correct is {correct}, total faces are {total} ")
cv.waitKey(0)





