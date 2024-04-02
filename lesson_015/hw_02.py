import cv2
import numpy as np

img = cv2.imread('images/color_text.jpg')
new_img = np.zeros(img.shape, np.uint8)

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
img = cv2.bitwise_and(img, img, mask=mask)

img = cv2.GaussianBlur(img, (7, 7), 0)
img = cv2.Canny(img, 250, 250)
# con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(new_img, con, -1, (0, 0, 255), 1)
#
# cropped_image = new_img[0:170, 0:new_img.shape[1]]
# cropped_image_2 = new_img[170:340, 0:new_img.shape[1]]
# # cropped_image = cropped_image[:, :, 255]



cropped_image = img[0:170, 0:img.shape[1]]
con, hir = cv2.findContours(cropped_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_img, con, -1, (0, 0, 255), 1)
#
# cropped_image_2 = img[170:340, 0:img.shape[1]]
# con, hir = cv2.findContours(cropped_image_2, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(cropped_image_2, con, -1, (255, 0, 0), 1)
# # cropped_image = cropped_image[:, :, 255]

# vis = np.concatenate((cropped_image, cropped_image_2), axis=0)


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


cv2.imshow('image', new_img)
cv2.waitKey(0)