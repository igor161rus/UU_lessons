import cv2
import numpy as np

logo = np.zeros((450, 450, 3), dtype=np.uint8)

dict_points = {
    'point_1': (logo.shape[1] // 3, logo.shape[0] // 3),
    'point_2': (int(logo.shape[1] // 2.5), logo.shape[0] // 3),
    'point_3': (logo.shape[1] // 3, int(logo.shape[0] // 3 * 1.5))}

print(dict_points['point_2'])

cv2.line(logo, dict_points['point_1'], dict_points['point_2'], (255, 255, 255), thickness=3)
cv2.line(logo, dict_points['point_1'], dict_points['point_3'], (255, 0, 0), thickness=1)


cv2.imshow('Logo', logo)
cv2.waitKey(0)