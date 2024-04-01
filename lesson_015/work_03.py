import cv2

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
cv2.imshow('image', img[0:100, 0:200])

# new_img = cv2.resize(img, (int(img.shape[1] * 0.5), int(img.shape[0] * 0.5)))
# cv2.imshow('image', new_img)
# cv2.imshow('image', img)
cv2.waitKey(1000)
