import cv2
import numpy as np
from pylibdmtx import pylibdmtx

# Ползунки без маски
# def nothing(args): pass
#
#
# cv2.namedWindow("setup")
# cv2.createTrackbar("b1", "setup", 0, 255, nothing)
# cv2.createTrackbar("g1", "setup", 0, 255, nothing)
# cv2.createTrackbar("r1", "setup", 0, 255, nothing)
# cv2.createTrackbar("b2", "setup", 255, 255, nothing)
# cv2.createTrackbar("g2", "setup", 255, 255, nothing)
# cv2.createTrackbar("r2", "setup", 255, 255, nothing)
#
# fn = 'images/20240403_202430.jpg'
# img = cv2.imread(fn)
# img = cv2.resize(img, (img.shape[1] // 10, img.shape[0] // 10))
#
# while True:
#     r1 = cv2.getTrackbarPos('r1', 'setup')
#     g1 = cv2.getTrackbarPos('g1', 'setup')
#     b1 = cv2.getTrackbarPos('b1', 'setup')
#     r2 = cv2.getTrackbarPos('r2', 'setup')
#     g2 = cv2.getTrackbarPos('g2', 'setup')
#     b2 = cv2.getTrackbarPos('b2', 'setup')
#
#     min_p = (g1, b1, r1)
#     max_p = (g2, b2, r2)
#
#     img_g = cv2.inRange(img, min_p, max_p)
#
#     cv2.imshow('img', img_g)
#
#     if cv2.waitKey(33) & 0xFF == ord('q'):
#         break
#
# cv2.destroyAllWindows()

# **************************************************************
# V2 ползунков

# def nothing(args): pass
#
#
# cv2.namedWindow("setup")
# cv2.createTrackbar("b1", "setup", 0, 255, nothing)
# cv2.createTrackbar("g1", "setup", 0, 255, nothing)
# cv2.createTrackbar("r1", "setup", 0, 255, nothing)
# cv2.createTrackbar("b2", "setup", 255, 255, nothing)
# cv2.createTrackbar("g2", "setup", 255, 255, nothing)
# cv2.createTrackbar("r2", "setup", 255, 255, nothing)
#
# fn = 'images/20240403_202430.jpg'
# img = cv2.imread(fn)
# img = cv2.resize(img, (img.shape[1] // 10, img.shape[0] // 10))
#
# while True:
#     r1 = cv2.getTrackbarPos('r1', 'setup')
#     g1 = cv2.getTrackbarPos('g1', 'setup')
#     b1 = cv2.getTrackbarPos('b1', 'setup')
#     r2 = cv2.getTrackbarPos('r2', 'setup')
#     g2 = cv2.getTrackbarPos('g2', 'setup')
#     b2 = cv2.getTrackbarPos('b2', 'setup')
#     min_p = (g1, b1, r1)
#     max_p = (g2, b2, r2)
#     img_mask = cv2.inRange(img, min_p, max_p)
#     img_m = cv2.bitwise_and(img, img, mask=img_mask)
#     cv2.imshow('img', img_m)
#     if cv2.waitKey(33) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()


# **********************************************************************
# V3 ползунков
# def nothing(args): pass
#
#
# cv2.namedWindow("setup")
# cv2.namedWindow("setup2")
# cv2.createTrackbar("b1", "setup", 0, 255, nothing)
# cv2.createTrackbar("g1", "setup", 0, 255, nothing)
# cv2.createTrackbar("r1", "setup", 0, 255, nothing)
# cv2.createTrackbar("b2", "setup", 255, 255, nothing)
# cv2.createTrackbar("g2", "setup", 255, 255, nothing)
# cv2.createTrackbar("r2", "setup", 255, 255, nothing)
# cv2.createTrackbar("blur", "setup2", 0, 10, nothing)
#
# fn = 'images/20240403_202430.jpg'
# img = cv2.imread(fn)
# img = cv2.resize(img, (img.shape[1] // 5, img.shape[0] // 5))
#
# percent = 50
# width = int(img.shape[1] * percent / 100)
# height = int(img.shape[0] * percent / 100)
# dim = (width, height)
# img = cv2.resize(img, dim)
# while True:
#     r1 = cv2.getTrackbarPos('r1', 'setup')
#     g1 = cv2.getTrackbarPos('g1', 'setup')
#     b1 = cv2.getTrackbarPos('b1', 'setup')
#     r2 = cv2.getTrackbarPos('r2', 'setup')
#     g2 = cv2.getTrackbarPos('g2', 'setup')
#     b2 = cv2.getTrackbarPos('b2', 'setup')
#     blur = cv2.getTrackbarPos('blur', 'setup2')
#     min_p = (g1, b1, r1)
#     max_p = (g2, b2, r2)
#     img_bl = cv2.medianBlur(img, 1 + blur * 2)
#     img_mask = cv2.inRange(img_bl, min_p, max_p)
#     img_m = cv2.bitwise_and(img, img, mask=img_mask)
#     cv2.imshow('img', img_m)
#     if cv2.waitKey(33) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()

# **********************************************************************

# Loading pictures

img = cv2.imread('images/20240403_202509.jpg')
img = cv2.resize(img, (img.shape[1] // 7, img.shape[0] // 7))
new_img = np.zeros(img.shape, np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mask = cv2.inRange(img, (196, 0, 0), (255, 255, 255))
img = cv2.bitwise_and(img, img, mask=mask)

# ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
ret, thresh = cv2.threshold(gray, 215, 230, cv2.THRESH_BINARY)
# con, hir = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.imshow('image', img)
cv2.imshow('gray', gray)
cv2.imshow('thresh', thresh)

cv2.waitKey(0)

all_barcode_info = pylibdmtx.decode(img, timeout=500, max_count=25)
print(len(all_barcode_info))
print(all_barcode_info)
for i in all_barcode_info:
    print(i.data.decode("utf-8"))

all_barcode_info = pylibdmtx.decode(thresh)
print(len(all_barcode_info))
print(all_barcode_info)
for i in all_barcode_info:
    print(i.data.decode("utf-8"))

all_barcode_info = pylibdmtx.decode(gray, timeout=500, max_count=25)
print(len(all_barcode_info))
print(all_barcode_info)
for i in all_barcode_info:
    print(i.data.decode("utf-8"))
