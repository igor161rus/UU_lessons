import cv2
import numpy as np

photo = cv2.imread('images/uu.JPG')
# img = np.zeros((350, 350), dtype=np.uint8)
img = np.zeros(photo.shape[:2], dtype=np.uint8)

circle = cv2.circle(img.copy(), (150, 150), 120, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=circle)
# img = cv2.bitwise_or(circle, square)
# img = cv2.bitwise_or(circle, square)
# img = cv2.bitwise_xor(circle, square)
# img = cv2.bitwise_not(square)

cv2.imshow('image', img)
cv2.waitKey(0)
