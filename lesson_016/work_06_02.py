import cv2

img_path = 'data/girl.jpg'
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
img = cv2.imread(img_path)

scale_percent = 40
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(10, 10)
)
for (x, y, w, h) in faces:
    cv2.rectangle(resized, (x, y), (x+w, y+h), (255, 255, 0), 2)
cv2.imshow('image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()