import cv2
import numpy as np

# img = cv2.imread('images/opencv.png')
# cv2.imshow('image', img)
# cv2.waitKey(1000)

# cap = cv2.VideoCapture('video/road.mov')
# while True:
#     success, frame = cap.read()
#     cv2.imshow('video', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
#
# while True:
#     ret, frame = cap.read()
#     cv2.imshow('webcam', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

img = cv2.imread('images/opencv.png')
# print(img.shape) # (512, 414, 3)
# new_img = cv2.resize(img, (300, 200))
# img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
img = cv2.resize(img, (int(img.shape[1] * 0.5), int(img.shape[0] * 0.5)))
# cv2.imshow('image', img[0:100, 0:200])
img = cv2.GaussianBlur(img, (9, 9), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 30, 30)

kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)

img = cv2.erode(img, kernel, iterations=1)

# new_img = cv2.resize(img, (int(img.shape[1] * 0.5), int(img.shape[0] * 0.5)))
# cv2.imshow('image', new_img)
cv2.imshow('image', img)
cv2.waitKey(1000)

# 1