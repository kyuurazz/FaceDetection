import cv2

# Memuat cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Untuk merekam video dari webcam. 
cap = cv2.VideoCapture(0)
# Untuk menggunakan file video sebagai input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Membaca Frame
    _, img = cap.read()

    # Ubah ke skala abu-abu
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Deteksi Wajah
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Gambarlah persegi panjang di sekitar setiap wajah
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Tampilan
    cv2.imshow('img', img)

    # Berhenti jika tombol escape ditekan
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Lepaskan objek VideoCapture
cap.release()