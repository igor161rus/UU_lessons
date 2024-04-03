import cv2
import numpy as np

cap = cv2.VideoCapture('video/videoplayback.mp4')

while True:
    success, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    faces_cascade = cv2.CascadeClassifier('faces.xml')

    faces = faces_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=7)
    eyes = eyes_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=7)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=1)

    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=1)

    cv2.imshow('result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
