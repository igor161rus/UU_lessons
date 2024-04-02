import cv2
import numpy as np

img = cv2.imread('images/color_text.jpg')
new_img_1 = np.zeros(img.shape, np.uint8)

# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv, (1, 1, 1), (255, 250, 250))
# new_img_mask = cv2.bitwise_and(img, img, mask=mask)
#
#
# new_img = cv2.cvtColor(new_img_mask, cv2.COLOR_BGR2GRAY)
# new_img = cv2.Canny(new_img, 250, 250)
# con, hir = cv2.findContours(new_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(new_img_1, con, -1, (255, 255, 0), 1)
#
# print(new_img_1.shape)
# cropped_image = new_img_1[0:170, 0:new_img_1.shape[1]]
# cropped_image = cropped_image[:, :, 0]
# cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_GRAY2BGR)
# b, g, r = cv2.split(cropped_image)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (1, 1, 1), (255, 250, 250))
new_img_mask = cv2.bitwise_and(img, img, mask=mask)

new_img = cv2.Canny(new_img_mask, 250, 250)
con, hir = cv2.findContours(new_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_img_1, con, -1, (255, 0, 0), 1)

cropped_image = new_img_1[0:170, 0:new_img_1.shape[1]]
# cropped_image = cropped_image[:, :, 255]

# # new_img = cv2.cvtColor(new_img_mask, cv2.COLOR_BGR2GRAY)
# new_img = cv2.Canny(new_img, 250, 250)
# con, hir = cv2.findContours(new_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(new_img_1, con, -1, (255, 255, 0), 1)
#
# print(new_img_1.shape)
# cropped_image = new_img_1[0:170, 0:new_img_1.shape[1]]
# cropped_image = cropped_image[:, :, 0]
# # cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_GRAY2BGR)
# b, g, r = cv2.split(cropped_image)


cv2.imshow('image', cropped_image)
cv2.waitKey(0)