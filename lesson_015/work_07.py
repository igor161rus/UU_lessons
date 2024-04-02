# github.com/opencv/opencv/tree/master/data/haarcascades

import cv2
img = cv2.imread('images/people.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('faces.xml')

result = faces.detectMultiScale(img, scaleFactor=2, minNeighbors=7)

for (x, y, w, h) in result:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)

cv2.imshow('image', img)
cv2.waitKey(0)