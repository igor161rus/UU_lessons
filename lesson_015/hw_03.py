import cv2
import numpy as np

left_eye_x = 0
right_eye_x = 0

cap = cv2.VideoCapture('video/test_1.mp4')

while True:
    success, img = cap.read()
    cut_eye = np.zeros(img.shape, np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    faces_cascade = cv2.CascadeClassifier('faces.xml')

    faces = faces_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=6)

    for (x, y, w, h) in faces:
        eyes = eyes_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=6)
        if len(eyes) >= 2:
            ex1, ey1, ew1, eh1 = eyes[0]
            ex2, ey2, ew2, eh2 = eyes[1]
            if faces[0][0] < ex1:
                eye = cv2.rectangle(img, (x, ey1), (x + w, ey1 + eh2), (0, 0, 0), thickness=1)
                cut_eye = eye[ey1:ey1 + eh2, x:x + w]
                cut_eye = cv2.GaussianBlur(cut_eye, (49, 49), 0)
                # eye[ey1:ey1 + eh2, x:x + w] = cv2.medianBlur(eye[ey1:ey1 + eh2, x:x + w], 35)
                cut_eye = cv2.cvtColor(cut_eye, cv2.COLOR_BGR2GRAY)
                cut_eye = cv2.cvtColor(cut_eye, cv2.COLOR_GRAY2BGR)
                img[ey1:ey1 + eh2, x:x + w] = cut_eye

    cv2.imshow('result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
