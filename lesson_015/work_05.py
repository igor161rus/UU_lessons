import cv2

img = cv2.imread('images/uu.JPG')

# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)

img = cv2.merge((r, g, b))

# cv2.imshow('image', r)
cv2.imshow('image', img)
cv2.waitKey(0)