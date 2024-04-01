import cv2
import numpy as np

# cap = cv2.VideoCapture('video/sample_video.mp4 (240p).mp4')
#
# while True:
#     success, img = cap.read()
#
# # img = cv2.resize(img, (int(img.shape[1] * 0.5), int(img.shape[0] * 0.5)))
#     img = cv2.GaussianBlur(img, (9, 9), 0)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     img = cv2.Canny(img, 30, 30)
#
#     kernel = np.ones((5, 5), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#
#     img = cv2.erode(img, kernel, iterations=1)
#
#     cv2.imshow('result', img)
#
#     # cv2.waitKey(0)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

img = cv2.imread('images/uu.JPG')


# img = cv2.flip(img, 1)
def rotate(img_param, angle):
    h, w = img_param.shape[:2]
    point = (w // 2, h // 2)

    m = cv2.getRotationMatrix2D(point, angle, 1.0)
    return cv2.warpAffine(img_param, m, (w, h))


def transform(img_param, x, y):
    h, w = img_param.shape[:2]
    m = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param, m, (w, h))


# img = rotate(img, 45)
img = transform(img, 30, 100)
cv2.imshow('image', img)
cv2.waitKey(0)
