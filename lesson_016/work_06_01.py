import cv2

img = cv2.imread('data/girl.jpg')


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


cropped = img[50:2500, 100:1500]
viewImage(cropped, 'cropped')

scale_percent = 20
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
viewImage(resized, 'resized')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
viewImage(gray_img, 'gray')

line = img.copy()
cv2.line(line, (0, 0), (2000, 2000), (255, 0, 0), 5)
viewImage(line, 'line')

rectangle = img.copy()
cv2.rectangle(rectangle, (4000, 50), (2000, 2000), (0, 255, 0), 5)
viewImage(rectangle, 'rectangle')

circle = img.copy()
cv2.circle(circle, (2000, 2000), 1000, (0, 0, 255), 5)
viewImage(circle, 'circle')

