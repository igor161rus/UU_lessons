import cv2
import numpy as np

left_eye_point_x = 0
right_eye_point_x = 0

cap = cv2.VideoCapture('video/videoplayback.mp4')

while True:
    success, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    faces_cascade = cv2.CascadeClassifier('faces.xml')

    faces = faces_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=7)
    # eyes = eyes_cascade.detectMultiScale(gray, scaleFactor=5, minNeighbors=2)

    # for (x, y, w, h) in faces:
    #     k1 = y + h // 3
    #     k2 = (y + h) // 2
    #     faces1 = cv2.rectangle(img, (x, y + h // 3), (x + w, (y + h) // 2), (0, 255, 0), thickness=1)
    #     # mask = cv2.inRange(faces, (1, 1, 1), (255, 250, 250))
    #     # gray = cv2.bitwise_and(img, img, mask=mask)
    #     x1 = faces1[0][0][0]
    #     y1 = faces1[0][1][0]
    #     w1 = faces1[0][2][0]
    #     h1 = faces1[0][3][0]
    #     print(x1, y1, w1, h1)
    #     faces1[y:y1 + h1, x:x1 + w1] = cv2.medianBlur(gray[y:y1 + h1, x:x1 + w1], 35)
    #     # faces1[y:y+h, x:x+w] = cv2.medianBlur(faces[y+h:, x:x+w], 35)

    # for (x, y, w, h) in eyes:
    #     eye = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=1)
    #     eye[y:y + h, x:x + w] = cv2.medianBlur(eye[y:y + h, x:x + w], 35)
    # for (ex, ey, ew, eh) in eyes:  # draws boxes around eyes

    for (x, y, w, h) in faces:  # draws box around face
        print('face', x, y, w, h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  #
        roi_gray = gray[y:y + h, x:x + w]
        # roi_color = img[y:y + h, x:x + w]
        eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=2, minNeighbors=2)  # looks for eyes
        for (x1, y1, w1, h1) in eyes:
            print('eye_1', x1, y1, w1, h1)
            eye = cv2.rectangle(img, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), thickness=1)
        for (ex, ey, ew, eh) in eyes:  # draws boxes around eyes
            print('eye', ex, ey, ew, eh)
            if (ex + ey) / 2 < (x + y) / 2:
                left_eye_point_x = ex
                print('left', left_eye_point_x)
            elif (ex + ey) / 2 > (x + y) / 2:
                right_eye_point_x = ex
                print('right', right_eye_point_x)
        cv2.line(img, (int(left_eye_point_x), int(right_eye_point_x)),
                 (int(left_eye_point_x), int(right_eye_point_x)), (0, 255, 0), 10)
    cv2.imshow('result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
