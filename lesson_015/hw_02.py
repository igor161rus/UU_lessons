import cv2
import numpy as np

img = cv2.imread('images/color_text.jpg')
new_img = np.zeros(img.shape, np.uint8)
# new_img = np.zeros((170, 340), np.uint8)
img_tmp = np.zeros(img.shape, np.uint8)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (1, 1, 1), (255, 250, 250))
img = cv2.bitwise_and(img, img, mask=mask)

img = cv2.GaussianBlur(img, (7, 7), 0)
img = cv2.Canny(img, 250, 250)
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_img, con, -1, (0, 255, 0), 1)
print(new_img.shape)

height, width, channels = new_img.shape

green = [0, 255, 0]
red = [0, 0, 255]
blue = [255, 0, 0]

for x in range(0, width):
    for y in range(0, 170):
        channels_xy = new_img[y, x]
        # print(channels_xy)
        if all(channels_xy == green):
            new_img[y, x] = red

    for y in range(305, 720):
        channels_xy = new_img[y, x]
        # print(channels_xy)
        if all(channels_xy == green):
            new_img[y, x] = blue

cv2.imwrite('images/hw_02.jpg', new_img)

cv2.imshow('image', new_img)
cv2.waitKey(0)
