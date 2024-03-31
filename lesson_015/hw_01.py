import cv2
import numpy as np


def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T


logo = np.zeros((480, 480, 3), dtype=np.uint8)
logo[:, :, 0] = get_gradient_2d(0, 150, logo.shape[0], logo.shape[0], True)
python_logo = cv2.imread("python.png")
python_logo = cv2.resize(python_logo, (logo.shape[1] // 3, logo.shape[0] // 4))
x, y = logo.shape[1] // 2 - python_logo.shape[1] // 2, logo.shape[0] // 2 - python_logo.shape[0] // 2
h, w = python_logo.shape[:2]
logo[y:y + h, x:x + w] = python_logo

dict_points = {
    'point_1': (logo.shape[1] // 6, logo.shape[0] // 4),
    'point_2': (logo.shape[1] // 3, logo.shape[0] // 4),
    'point_3': (int(logo.shape[1] // 1.5), logo.shape[0] // 4),
    'point_4': (int(logo.shape[1] // 1.2), logo.shape[0] // 4),
}

cv2.line(logo, dict_points['point_1'], dict_points['point_2'], (0, 0, 255), thickness=2)
cv2.line(logo, dict_points['point_3'], dict_points['point_4'], (0, 0, 255), thickness=2)
for i in dict_points:
    cv2.line(logo, dict_points[i], (dict_points[i][0], dict_points[i][1] * 2), (255, 0, 0), thickness=2)

cv2.ellipse(logo, (logo.shape[1] // 2, logo.shape[0] // 2),
            (dict_points['point_1'][0], dict_points['point_1'][0]),
            0, 0, 180, (0, 255, 0), thickness=2)
cv2.ellipse(logo, (logo.shape[1] // 2, logo.shape[0] // 2),
            (dict_points['point_2'][0], dict_points['point_2'][0]),
            0, 0, 180, (0, 255, 0), thickness=2)

cv2.circle(logo, (logo.shape[1] // 2, logo.shape[0] // 2), logo.shape[1] // 2, (255, 255, 0), thickness=2)

cv2.imshow('Logo', logo)
cv2.waitKey(0)
