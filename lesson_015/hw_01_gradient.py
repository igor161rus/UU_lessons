import cv2
import numpy as np

logo = np.zeros((480, 480, 3), dtype=np.uint8)

dict_points = {
    'point_1': (logo.shape[1] // 6, logo.shape[0] // 4),
    'point_2': (logo.shape[1] // 3, logo.shape[0] // 4),
    'point_3': (int(logo.shape[1] // 1.5), logo.shape[0] // 4),
    'point_4': (int(logo.shape[1] // 1.2), logo.shape[0] // 4),
}

# python_logo = cv2.imread("python_logo1.png")
#
# python_logo = cv2.resize(python_logo, (logo.shape[1] // 3, logo.shape[0] // 4))
# x, y = logo.shape[1] // 2 - python_logo.shape[1] // 2, logo.shape[0] // 2 - python_logo.shape[0] // 2
# h, w = python_logo.shape[:2]
#
# logo[y:y + h, x:x + w] = cv2.addWeighted(logo[y:y + h, x:x + w], 0.5, python_logo, 0.5, 0)
# logo[y:y + h, x:x + w] = python_logo

i = 0
k = 0
for _ in range(50):
    # logo[:, 0 + i:50 + i] = logo[y:y + h, x:x + w] = (255 - k, 255 - k, 255 - k)
    # logo[y:y + h, x:x + w] = (255 - k, 255 - k, 255 - k)
    logo[:, 0 + i:50 + i] = (255 - k, 255 - k, 255 - k)
    i += 20
    k += 5

# rows,cols,channels = python_logo.shape
# overlay=cv2.addWeighted(logo[250:250+rows, 0:0+cols],0.5,python_logo,0.5,0)
# logo[250:250+rows, 0:0+cols] = overlay

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
