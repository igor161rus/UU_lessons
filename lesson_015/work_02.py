import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype=np.uint8)

# RGB - Red, Green, Blue
# BGR - Blue, Green, Red - for OpenCV
photo[:] = [119, 201, 105]
photo[100:300, 100:300] = [255, 255, 255]

cv2.rectangle(photo, (100, 100), (300, 300), (0, 0, 255), thickness=3)
cv2.rectangle(photo, (10, 10), (30, 30), (0, 0, 255), thickness=-cv2.FILLED)

cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (0, 0, 255), thickness=3)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (0, 0, 255), thickness=-1)

cv2.putText(photo, 'OpenCV', (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('Photo', photo)
cv2.waitKey(0)

