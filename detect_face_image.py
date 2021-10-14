import cv2

# Memuat cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Input foto
img = cv2.imread('test.jpg')

# Ubah ke skala abu-abu
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Deteksi Wajah
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Gambarlah persegi panjang di sekitar setiap wajah
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Tampilan output
cv2.imshow('img', img)
cv2.waitKey()
